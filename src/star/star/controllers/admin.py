from flask import Flask, render_template, render_template_string, jsonify, redirect, url_for, request, send_from_directory, session
from star import app
from star.views import render
from star.views import admin as admin_views
from star.models.dal.post import PostPrivateDAL
from star.models.dal.user import UserPrivateDAL
from star.lib import ajax
from werkzeug import secure_filename
import os

@app.route('/admin', methods=['GET'])
def admin_dashboard():
    #if not session.get('logged_in'):
    #    return url_for('login')
    data = {"project_name": "Hello World"}
    return render(admin_views.admin_dashboard, data)

@app.route('/work', methods=['POST'])
def create_work():
    if not request.is_xhr:
        return url_for('login')

    user = UserPrivateDAL.getUserByUserID(1) # TODO Should use the logged-in user
    form = request.form
    title    = form.get('title', '')
    subtitle = form.get('subtitle', '')
    content  = form.get('content', '')
    summary  = form.get('summary', '')
    excerpt  = '' # TODO Need a better way to extract text from the HTML content
    metadata = form.get('metadata', '')
    post = PostPrivateDAL.addPost(user.id, title, excerpt, content, '', '', '')
    # TODO Add tags and categories to the post

    cover_image = request.files.get('cover-image', None)
    cover_image_url = ""
    if cover_image:
        filename = secure_filename(cover_image.filename)
        # NOTE There's a race condition
        # http://stackoverflow.com/questions/273192/create-directory-if-it-doesnt-exist-for-file-write
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        # TODO Make sure the filename is unique and won't overwrite existing files
        cover_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cover_image_url = url_for('uploaded_file', filename=filename)
    # TODO Default value of cover_image_url
    work = PostPrivateDAL.addWork(post.id, subtitle, summary, cover_image_url, metadata)
    return render(jsonify, ajax.payload("success"))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
