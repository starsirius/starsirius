from flask import Flask, render_template, render_template_string
from star import app
from star.views import render
from star.views import site as site_views

@app.route('/', methods=['GET'])
def index():
    data = {"project_name": "Hello World"}
    return render(site_views.index, data)

@app.route('/login', methods=['GET'])
def login():
    data = {"project_name": "Hello World"}
    return render(site_views.login, data)

@app.errorhandler(404)
def not_found(error):
    return render(site_views.not_found, 404)

@app.errorhandler(500)
def internal_server_error(error):
    return render(site_views.internal_server_error, 500)
