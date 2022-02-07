""" from routes.algorithms.utils.frontend_data_parser import parse_input


def decorate2(request, function):
    def wrap_function(*args, **kwargs):
        body = parse_input(request.json)
        if body["status_code"] != 200:
            return body["error"], body["status_code"]
        data = body["data"]
        kwargs["data"] = data
        kwargs["pbi_ids"] = data["pbi_ids"]
        return function(*args, **kwargs)

    return wrap_function


import functools
 """

""" def decorate(request):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(request)
            body = parse_input(request.json)
            if body["status_code"] != 200:
                return body["error"], body["status_code"]
            data = body["data"]
            kwargs["data"] = data
            kwargs["pbi_ids"] = data["pbi_ids"]
            return function(*args, **kwargs)

        return wrapper

    return actual_decorator """
