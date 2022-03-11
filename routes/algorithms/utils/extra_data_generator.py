from typing import List
import evaluation.metrics as metrics
from models.Solution import Solution
from algorithms.abstract_algorithm.abstract_algorithm import AbstractAlgorithm


def get_metrics(population: List[Solution]) -> List[dict]:
    result = []
    result.append(
        {
            "code": "hv",
            "name": "Hypervolume",
            "value": metrics.calculate_hypervolume(population),
        }
    )
    result.append(
        {
            "code": "spread",
            "name": "Spread",
            "value": metrics.calculate_spread(population),
        }
    )
    result.append(
        {
            "code": "spacing",
            "name": "Spacing",
            "value": metrics.calculate_spacing(population),
        }
    )
    result.append(
        {
            "code": "nsols",
            "name": "# Solutions",
            "value": metrics.calculate_numSolutions(population),
        }
    )
    return result


def get_hyperparameters(algorithm: AbstractAlgorithm) -> List[dict]:
    formatted_hyperparameters = [hp.to_dict() for hp in algorithm.hyperparameters]
    for fh in formatted_hyperparameters:
        if fh["name"] in ["MaxEvaluations", "MaxGenerations"]:
            if fh["value"] == 0:
                fh["value"] = "-"
    return formatted_hyperparameters
