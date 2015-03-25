from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, lm

class User(UserMixin, db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	passwordHash = db.Column(db.String(128))
	balance = db.Column(db.Integer, default = 10000)

	@property
	def password(self):
		raise AttributeError("Password is not a readable attribute")

	@password.setter
	def password(self, password):
		self.passwordHash = generate_password_hash(password)

	def VerifyPassword(self, password):
		return check_password_hash(self.passwordHash, password)

	def IncreaseBalance(self, amount):
		self.balance += amount

	def DecreaseBalance(self, amount):
		self.balance -= amount

	def __repr__(self): return "<User {}>".format(self.name)

@lm.user_loader
def LoadUser(id):
	return User.query.get(int(id))