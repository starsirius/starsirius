from flask import render_template, render_template_string

def admin_dashboard(data_dict):
    """
    Generates the html string for the homepage given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/admin.html', **data_dict)
