from typing import Any, Dict
from datasets.Dataset import Dataset
from algorithms.genetic.geneticnds.geneticnds_algorithm import (
    GeneticNDSAlgorithm,
)


def solve_post(data) -> Dict[str, Any]:

    dataset = Dataset(source_dict=data)

    algorithm = GeneticNDSAlgorithm(
        dataset=dataset,
        tackle_dependencies=False,
        population_length=100,
        max_generations=100,
        max_evaluations=0,
        crossover_prob=0.8,
        mutation="flipeachbit",
        mutation_prob=1.0,
    )
    algorithm.dataset = dataset

    result = algorithm.run()

    return algorithm, result
