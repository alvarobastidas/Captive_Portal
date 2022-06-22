from backend.constants import Admins, Clients
from backend import bcrypt


def login_process(username, password):
    user = Admins.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return False


def clients_data():
    return Clients.query
