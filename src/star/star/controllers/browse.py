from flask import Flask, jsonify, redirect, url_for
from star import app
from star.views import render
from star.views import browse as browse_views
from star.models.dal.post import PostPrivateDAL

@app.route('/portfolio', methods=['GET'])
def browse_portfolio():
    works = PostPrivateDAL.getWorks()
    data = {"works": works}
    return render(browse_views.browse_portfolio, data)
