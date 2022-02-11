from typing import Any, Dict
from datasets.Dataset import Dataset
from algorithms.EDA.FEDA.feda_algorithm import (
    FEDAAlgorithm,
)


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = FEDAAlgorithm(
        dataset=dataset,
        tackle_dependencies=True,
        population_length=100,
        max_generations=100,
        max_evaluations=0,
        selected_individuals=60,
        selection_scheme="nds",
    )
    algorithm.dataset = dataset

    result = algorithm.run()

    return result
