"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, filefolder
from flask import render_template, request, redirect, url_for, flash
from forms import ProfileForm
from werkzeug.utils import secure_filename
from models import UserProfile
import os
import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        fname=form.first_name.data
        lname=form.last_name.data
        email=form.email.data
        gender=form.gender.data
        location=form.location.data
        bio=form.bio.data
        fileupd = form.image.data
        filename = secure_filename(fileupd.filename)
        created=datetime.datetime.now()
        user=user = UserProfile(first_name=fname, last_name=lname, gender=gender, email=email, location=location, biography=bio, image_url=filename, created_on=created)
        db.session.add(user)
        db.session.commit()
        fileupd.save(os.path.join(filefolder, filename))
        flash('User added successfully','success')
        return redirect(url_for('profiles')) 
    flash_errors(form)
    return render_template("profile.html", form=form)



@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    return render_template('profiles.html', users=users)
    
    
@app.route("/profiles/<filename>")
def user_profile(filename):
    user = UserProfile.query.filter_by(id=filename).first()
    return render_template('user_profile.html', user=user)
    
    
###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
