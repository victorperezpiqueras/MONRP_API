from typing import Tuple, Dict, Any


def parse_body(body: Dict) -> Dict[Any, int]:
    if not all(
        key in body
        for key in (
            "pbi_costs",
            "stakeholder_importances",
            "stakeholder_pbis_priorities",
        )
    ):
        return {
            "error": "Body format must include:pbi_costs[],stakeholder_importances[],stakeholder_pbis_priorities[]",
            "status_code": 400,
        }

    return {
        "data": body,
        "status_code": 200,
    }
