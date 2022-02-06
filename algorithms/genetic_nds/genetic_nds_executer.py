import json

from algorithms.utils.algorithm_parser import algorithm_parser

from algorithms.genetic_nds.genetic_nds_algorithm import GeneticNDSAlgorithm

from algorithms.models.problem import Problem

def GeneticNDS_executer(stakeholder_importances, pbi_stakeholder_values, pbis):
    print("GeneticNDS running...")

    genes, warning = algorithm_parser(stakeholder_importances,pbi_stakeholder_values, pbis)
    objectives_minimization = ["MAX", "MIN"]

    #print(genes)

    problem = Problem(genes, objectives_minimization)

    #algorithm = GeneticNDSAlgorithm(problem, random_seed=None, population_length=30, 
    #                            max_generations=100, crossover="onepoint", crossover_prob=0.6,
    #                            mutation="flip1bit", mutation_prob=0.1,replacement="elitismnds")
    algorithm = GeneticNDSAlgorithm(problem, random_seed=None, population_length=20, 
                                max_generations=100, crossover="onepoint", crossover_prob=0.6,
                                mutation="flip1bit", mutation_prob=0.7,replacement="elitismnds")


    algorithm_result = algorithm.run()

    # for i in algorithm_result["population"]:
    #    print(i)

    algorithm_result["warning"] = warning
    print("GeneticNDS ended...")

    return algorithm_result
