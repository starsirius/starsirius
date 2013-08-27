from flask import Flask, jsonify, redirect, url_for
from star import app
from star.views import render
from star.views import browse as browse_views
from star.models.dal.post import PostPrivateDAL

@app.route('/blog', methods=['GET'])
def browse_blog():
    data = {}
    return render(browse_views.browse_blog, data)

@app.route('/ux', methods=['GET'])
def browse_ux_posts():
    data = {}
    return render(browse_views.browse_ux_posts, data)

@app.route('/front-end-development', methods=['GET'])
def browse_front_end_development_posts():
    data = {}
    return render(browse_views.browse_front_end_development_posts, data)

@app.route('/portfolio', methods=['GET'])
def browse_portfolio():
    works = PostPrivateDAL.getWorks()
    data = {"works": works}
    return render(browse_views.browse_portfolio, data)

