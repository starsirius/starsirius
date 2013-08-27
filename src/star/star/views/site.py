from flask import render_template, render_template_string

def index(data_dict):
    """
    Generates the html string for the homepage given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/index.html', **data_dict)

def login(data_dict):
    """
    Generates the html string for the login page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/login.html', **data_dict)

def not_found(data_dict):
    """
    Return the 404 Not Found string
    """
    return "404, I can't find that resource"

def internal_server_error(data_dict):
    """
    Return the 500 Server Error string
    """
    return "500, you bent my wookie (server error)"
