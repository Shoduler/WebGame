from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Required, Length, NumberRange
from app import db

class LoginForm(Form):
	username = StringField("Username", validators = [Required(), Length(1, 64)])
	password = PasswordField("Password", validators = [Required()])
	rememberMe = BooleanField("Remember me?")
	submit = SubmitField("Log In")

class BetForm(Form):
	amount = IntegerField("Amount", validators = [Required(), NumberRange(0, 1000)])
	number = IntegerField("Number (1-6)", validators = [Required(), NumberRange(1, 6)])
	submit = SubmitField("Bet")