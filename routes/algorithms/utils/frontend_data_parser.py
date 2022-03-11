from typing import List, Dict, Any
from models.Solution import Solution

from routes.algorithms.utils.extra_data_generator import (
    get_hyperparameters,
    get_metrics,
)
from algorithms.abstract_algorithm.abstract_algorithm import AbstractAlgorithm


def parse_input(body: Dict) -> Dict[str, Any]:
    if not body:
        return {
            "error": {"msg": "Body required"},
            "status_code": 400,
        }

    if not all(
        key in body
        for key in (
            "pbis",
            "importancias",
            "valores",
        )
    ):
        return {
            "error": "Body format must include:pbis[],importancias[],valores[]",
            "status_code": 400,
        }

    pbi_costs = []
    pbi_ids = []
    for pbi in body["pbis"]:
        pbi_costs.append(pbi["estimacion"])
        pbi_ids.append(pbi["idpbi"])

    # if pbis without cost -> asign max cost
    max_cost = max(filter(lambda v: v is not None, pbi_costs))
    # store warning if any pbi not estimated
    any_pbi_without_cost = any(cost is None for cost in pbi_costs)
    pbi_costs = [max_cost if cost is None else cost for cost in pbi_costs]

    stakeholder_importances = []
    stakeholder_importances_ids = []
    for imp in body["importancias"]:
        stakeholder_importances.append(imp["importancia"])
        stakeholder_importances_ids.append(imp["idrol"])

    stakeholders_pbis_priorities = [
        [0 for _ in range(len(pbi_costs))]
        for _ in range(len(stakeholder_importances_ids))
    ]
    for x in range(len(stakeholder_importances)):
        for y in range(len(pbi_costs)):
            values = [
                val["valor"]
                for val in body["valores"]
                if val["idpbi"] == pbi_ids[y]
                and val["idrol"] == stakeholder_importances_ids[x]
            ]
            # if no priority is given to a pbi -> set zero value
            stakeholders_pbis_priorities[x][y] = values[0] if len(values) > 0 else 0

    return {
        "data": {
            "pbis_cost": pbi_costs,
            "pbi_ids": pbi_ids,
            "stakeholders_importances": stakeholder_importances,
            "stakeholders_pbis_priorities": stakeholders_pbis_priorities,
            "warning": any_pbi_without_cost,
        },
        "status_code": 200,
    }


def parse_output(
    algorithm: AbstractAlgorithm, result: dict, data: dict
) -> Dict[str, Any]:
    population: List[Solution] = result["population"]

    returned_population = []
    for solution in population:

        total_cost = float(solution.dataset.pbis_cost[(solution.selected == 1)].sum())
        total_satisfaction = float(
            solution.dataset.pbis_satisfaction[(solution.selected == 1)].sum()
        )

        returned_solution = {
            "pbis": [],
            "satisfaction": total_satisfaction,
            "cost": total_cost,
        }
        for i in range(len(solution.selected)):
            returned_solution["pbis"].append(
                {
                    "idpbi": int(data["pbi_ids"][i]),
                    "included": int(solution.selected[i]),
                }
            )
        returned_population.append(returned_solution)

    parsed_result = {}
    parsed_result["population"] = returned_population
    parsed_result["warning"] = data["warning"]
    parsed_result["metrics"] = get_metrics(population)
    parsed_result["hyperparameters"] = get_hyperparameters(algorithm)
    return parsed_result
