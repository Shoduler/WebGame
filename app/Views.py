import random
from flask import redirect, request, render_template, flash, url_for, g
from flask_login import current_user, login_user, logout_user, login_required

from app import *
from app.Forms import LoginForm, BetForm
from app.Models import User

lm.login_view = "Login"

@app.before_request
def BeforeRequest():
	g.user = current_user

@app.route("/login", methods = ["GET", "POST"])
def Login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and user.VerifyPassword(form.password.data):
			login_user(user, form.rememberMe.data)
			return redirect(url_for("Index"))
		flash("Invalid username or password.")
	return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def Logout():
	logout_user()
	flash("You have been logged out.")
	return redirect(url_for("Index"))

@app.route("/", methods = ["GET", "POST"])
@login_required
def Index():
	form = BetForm()
	if form.validate_on_submit():
		amount = int(form.amount.data)
		prevBalance = g.user.balance
		result = random.randint(1, 6)
		if int(form.number.data) == result:
			g.user.balance += amount
			message = "You won {}$!".format(amount)
		else:
			g.user.balance -= amount
			message = "You lost {}$.".format(amount)
		db.session.commit()
		return render_template("index.html", prevBalance = prevBalance, balance = g.user.balance, form = BetForm(), result = result, message = message)
	return render_template("index.html", balance = g.user.balance, form = form)