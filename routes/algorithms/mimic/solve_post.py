from typing import Any, Dict
from datasets.Dataset import Dataset
from algorithms.EDA.bivariate.MIMIC.mimic_algorithm import (
    MIMICAlgorithm,
)


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = MIMICAlgorithm(
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
