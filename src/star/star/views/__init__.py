from flask import make_response, jsonify

def render(view_func, status=200, *data_dicts):
    """
    Wrap the result of a view function as a Flask response object,
    given the view function, status code, and data dict that will passed to the function
    Argument:
        view_func - a function, the function for generating a html string of a view (as found in the view files)
        [status] - an int, the HTTP status code [200]
        data_dicts - a variable-len list of dictionaries, the data dictionaries to pass to the view_func. These get flattened into a single dict.
    Return:
        a response_class object, the real response object
    Notes:
        The view_func needs to return a string
    """
    initial_dict = {}
    if isinstance(status, dict):
        initial_dict.update(status)
        status = 200
    data_dict = reduce(lambda old, new: dict(old, **new), data_dicts, initial_dict)
    if view_func == jsonify:
        return jsonify(**data_dict)
    html_str = view_func(data_dict) or "Your view function (%s) needs to return a string" % view_func.__name__
    return render_string(html_str, status)

def render_string(html_str, status=200):
    """
    Wrap a [most likely html] string as a Flask response object with status code
    Arguments:
        html_str - a string, the html string to be used as the body of the response
        [status] - a int, the status code of the response [200]
    Returns:
        res - a response_class object, the real response object
"""
    res = make_response(html_str, status)
    return res
