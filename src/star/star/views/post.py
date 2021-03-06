from flask import render_template, render_template_string

def work(data_dict):
    """
    Generates the html string for the work page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/portfolio-work.html', **data_dict)
