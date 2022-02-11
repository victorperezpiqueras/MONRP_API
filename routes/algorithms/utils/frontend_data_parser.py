from typing import List, Dict, Any
from models.Solution import Solution


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


def parse_output(result: Dict, data: dict) -> Dict[str, Any]:
    population: List[Solution] = result["population"]

    returned_population = []
    for solution in population:
        returned_solution = []
        for i in range(len(solution.selected)):
            returned_solution.append(
                {
                    "idpbi": int(data["pbi_ids"][i]),
                    "included": int(solution.selected[i]),
                }
            )
        returned_population.append(returned_solution)

    return {"population": returned_population, "warning": data["warning"]}
