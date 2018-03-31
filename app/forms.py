from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ProfileForm(FlaskForm):
    first_name = StringField('Firstname', validators=[InputRequired(message='First Name is required')])
    last_name = StringField('Lastname', validators=[InputRequired(message='Last Name is required')])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[InputRequired(message='Gender is required')])
    email = StringField('Email', validators=[InputRequired(message='Email is required'), Email(message="Only Emails")])
    location = StringField('Location', validators=[InputRequired(message='Location is required')])
    bio = TextAreaField('Biography', validators=[InputRequired(message='Location is required')])
    image = FileField('Image', validators=[FileRequired('Please input a file'), FileAllowed(['jpg', 'png'], 'Images only!')])