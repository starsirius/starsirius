from flask import Flask, jsonify, redirect, url_for
from star import app
from star.views import render
from star.views import post as post_views
from star.models.dal.post import PostPrivateDAL

@app.route('/work/<int:work_id>', methods=['GET'])
def work(work_id):
    work = PostPrivateDAL.getWorkByWorkID(work_id)
    if not work:
        pass
    data = {"work": work}
    return render(post_views.work, data)
