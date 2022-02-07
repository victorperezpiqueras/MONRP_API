from typing import Any, Dict
from src.monrp.datasets.Dataset import Dataset
from src.monrp.algorithms.genetic.geneticnds.geneticnds_algorithm import (
    GeneticNDSAlgorithm,
)
from src.monrp.algorithms.GRASP.GRASP import GRASP


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = GRASP(
        dataset=dataset,
        tackle_dependencies=False,
        solutions_per_iteration=100,
        iterations=100,
        max_evaluations=0,
        init_type="stochastically",
        local_search_type="best_first_neighbor_random_domination",
        path_relinking_mode="after_local",
    )
    algorithm.dataset = dataset

    result = algorithm.run()

    return result
