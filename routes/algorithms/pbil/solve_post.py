from typing import Any, Dict
from src.monrp.datasets.Dataset import Dataset
from src.monrp.algorithms.EDA.PBIL.pbil_algorithm import (
    PBILAlgorithm,
)


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = PBILAlgorithm(
        dataset=dataset,
        tackle_dependencies=False,
        population_length=100,
        max_generations=100,
        max_evaluations=0,
        learning_rate=0.5,
        mutation_prob=0.1,
        mutation_shift=0.1,
    )
    algorithm.dataset = dataset

    result = algorithm.run()

    return result
