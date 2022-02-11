from typing import Any, Dict
from datasets.Dataset import Dataset
from algorithms.EDA.UMDA.umda_algorithm import (
    UMDAAlgorithm,
)


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = UMDAAlgorithm(
        dataset=dataset,
        tackle_dependencies=False,
        population_length=100,
        max_generations=100,
        max_evaluations=0,
        selected_individuals=60,
        selection_scheme="nds",
        replacement_scheme="replacement",
    )
    algorithm.dataset = dataset

    result = algorithm.run()

    return result
