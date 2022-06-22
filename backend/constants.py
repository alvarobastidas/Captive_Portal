from backend import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(int(user_id))


class Constants:
    COMPANY_NAME = "El Arbolito"


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    movil = db.Column(db.String(10), nullable=False)
    ip = db.Column(db.String(20))
    mac = db.Column(db.String(40))
    device = db.Column(db.String(20))
    _date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"Clients('{self.name}', '{self.lastname}','{self.email}'," \
               f"'{self.movil}', '{self.mac}', '{self._date}')"


class Admins(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return f"Admins('{self.name}', '{self.lastname}','{self.email}')"


