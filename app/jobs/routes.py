from flask import Blueprint, redirect, render_template, url_for
from .models import Job

blueprint = Blueprint('jobs', __name__)

@blueprint.route('/jobs')
def choose_job():
    #Log:
    print('CHOOSE YOUR JOB')

    all_jobs = Job.query.all()
    return render_template("jobs/choose_job.html", all_jobs=all_jobs)

@blueprint.route('/play')
def play():
    # Log:
    print('REDIRECT /play TO /jobs')

    return redirect(url_for('jobs.choose_job'))

@blueprint.route('/jobs/<slug>')
def job_dynamic(slug):
    # Set variables for the template:
    job = Job.query.filter_by(slug=slug).first_or_404()

    # Log:
    print(F'CHOSE {job.name.upper()} AS JOB, HERE ARE YOUR STATS')

    return render_template("jobs/job_dynamic.html", job=job)