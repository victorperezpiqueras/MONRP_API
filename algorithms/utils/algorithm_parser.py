from algorithms.models.gen import Gen


def algorithm_parser(stakeholder_importances, pbi_stakeholder_values, pbis):
    # importancias de stakeholders
    '''
    {
        "idimportancia": 1,
        "idproyecto": 2,
        "idrol": 3,
        "importancia": 5
    }
    '''
    # estimaciones de pbis--------------------------------------------------------
    '''
    {
        "idpbi": 1,
        "titulo": "PBI 1-historia de usuario de ejemplo",
        "descripcion": null,
        "done": 1,
        "prioridad": 5,
        "label": "feature",
        "estimacion": 13,
        "valor": null,
        "sprint": 5,
        "sprintCreacion": 1,
        "idproyecto": 2,
        "idrelease": 9
    }
    '''
    # valores de pbis para cada stakeholder---------------------------------------
    '''
    {
        "idvalor": 5,
        "idpbi": 3,
        "idrol": 4,
        "valor": 5
    }
    '''
    # calcular estimacion maxima:----------------------------------------------------------
    max_estimacion = 0
    for i in range(0, len(pbis)):
        if pbis[i]["estimacion"] is not None \
                and pbis[i]["estimacion"] > max_estimacion:
            max_estimacion = pbis[i]["estimacion"]

    # creacion de genes:----------------------------------------------------------
    warning = False
    genes = []
    for i in range(0, len(pbis)):
        total_value = 0
        for j in range(0, len(stakeholder_importances)):
            importance = stakeholder_importances[j]["importancia"]
            value = 0
            for val in pbi_stakeholder_values:
                if val["idrol"] == stakeholder_importances[j]["idrol"] \
                        and val["idpbi"] == pbis[i]["idpbi"]:
                    value = val["valor"]
                    break

            total_value += importance*value

        total_value /= len(stakeholder_importances)+1

        # convertir estimaciones nulas a max_estimacion
        estimacion = pbis[i]["estimacion"]
        if estimacion is None:
            estimacion = max_estimacion
            warning = True

        new_gen = Gen(pbis[i]["idpbi"], total_value, estimacion)
        # print(new_gen)
        genes.append(new_gen)
        # print(new_gen)

    return genes, warning
