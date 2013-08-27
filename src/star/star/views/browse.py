from flask import render_template, render_template_string

def browse_blog(data_dict):
    """
    Generates the html string for the blog page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/blog-browse.html', **data_dict)

def browse_ux_posts(data_dict):
    """
    Generates the html string for the UX page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/ux-browse.html', **data_dict)

def browse_front_end_development_posts(data_dict):
    """
    Generates the html string for the front-end dev page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/front-end-dev-browse.html', **data_dict)

def browse_portfolio(data_dict):
    """
    Generates the html string for the portfolio page given a data dictionary.
    Arguments:
        data_dict - a dictionary, the data to be used in the html template
    Return:
        res - a string, the html string of the view
    """
    return render_template('templates/portfolio-browse.html', **data_dict)

