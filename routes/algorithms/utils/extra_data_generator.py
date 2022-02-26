from typing import List
import evaluation.metrics as metrics
from models.Solution import Solution


def get_metrics(population: List[Solution]):
    result = {}
    result["hv"] = metrics.calculate_hypervolume(population)
    result["spread"] = metrics.calculate_spread(population)
    result["spacing"] = metrics.calculate_spacing(population)
    result["nsols"] = metrics.calculate_numSolutions(population)
    return result
