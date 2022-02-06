import json

from algorithms.utils.algorithm_parser import algorithm_parser

from algorithms.nsgaii.nsgaii_algorithm import NSGAIIAlgorithm

from algorithms.models.problem import Problem


def NSGAII_executer(stakeholder_importances, pbi_stakeholder_values, pbis):
    print("NSGAII running...")

    genes, warning = algorithm_parser(stakeholder_importances,
                                   pbi_stakeholder_values, pbis)
    objectives_minimization = ["MAX", "MIN"]

    # for i in genes:
    #   print(i)

    problem = Problem(genes, objectives_minimization)

    algorithm = NSGAIIAlgorithm(problem, random_seed=None, population_length=30, 
                                max_generations=200, crossover="onepoint", crossover_prob=0.6,
                                mutation="flipeachbit", mutation_prob=0.05,replacement="elitism")

    algorithm_result = algorithm.run()

    # for i in algorithm_result["population"]:
    #    print(i)

    algorithm_result["warning"] = warning
    print("NSGAII ended...")

    return algorithm_result
