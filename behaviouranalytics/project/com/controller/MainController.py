from project import app
from flask import render_template


@app.route('/')
def adminLoadDashboard():
    return render_template('admin/index.html')


@app.route('/admin/viewUser')
def adminViewUser():
    return render_template('admin/viewUser.html')


@app.route('/admin/addDataset')
def adminAddDataset():
    return render_template('admin/addDataset.html')


@app.route('/admin/viewDataset')
def adminViewDataset():
    return render_template('admin/viewDataset.html')


@app.route('/admin/manageVideo')
def adminManageVideo():
    return render_template('admin/manageVideo.html')


@app.route('/admin/manageComplaint')
def adminManageComplaint():
    return render_template('admin/manageComplaint.html')


@app.route('/admin/replyComplaint')
def adminReplyComplaint():
    return render_template('admin/replyComplaint.html')


@app.route('/admin/manageFeedback')
def adminManageFeedback():
    return render_template('admin/manageFeedback.html')


@app.route('/admin/manageDetection')
def adminManageDetection():
    return render_template('admin/manageDetection.html')

