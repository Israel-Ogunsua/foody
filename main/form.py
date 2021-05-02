from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo, Length

class loginForm(FlaskForm):
    username = StringField(label ="Username", validators=[ DataRequired(), Length(min = 2, max= 40)])
    email =StringField(label= "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label= "Password", validators=[DataRequired()])
    submit = SubmitField(label= "Login")

class registrationForm():
    username = StringField(label ="Username", validators=[ DataRequired(), Length(min = 2, max= 40)])
    email =StringField(label= "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label= "Password", validators=[DataRequired()])
    repassword =PasswordField(label="Confirm Password", validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField(label= "Login")

    