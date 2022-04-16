from flask import Blueprint, redirect, render_template, url_for, request
from .models import Job

blueprint = Blueprint('jobs', __name__)

### CHOOSE JOB ###
@blueprint.route('/jobs')
def choose_job():
    # Variables for template
    page_number = request.args.get('page', 1, type=int) # pagination ?
    all_jobs = Job.query.all()

    # View
    return render_template("jobs/choose_job.html", all_jobs=all_jobs)

@blueprint.route('/play')
def job_redirect():
    return redirect(url_for('jobs.choose_job'))


### JOB VIEW ###
@blueprint.route('/jobs/<slug>')
def job_dynamic(slug):
    # Variables for template
    job = Job.query.filter_by(slug=slug).first_or_404()

    # View
    return render_template("jobs/job_dynamic.html", job=job)