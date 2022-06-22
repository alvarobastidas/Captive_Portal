from backend.constants import Clients
from backend import db
from datetime import datetime, timedelta


def save_info_db(name, lastname, email, movil, ip, mac, device):
    client = Clients(
        name=name,
        lastname=lastname,
        email=email,
        movil=movil,
        ip=ip,
        mac=mac,
        device=device,
        _date=datetime.now()
    )
    db.session.add(client)
    db.session.commit()


def check_last_clients():
    three_hours_ago = datetime.now() - timedelta(hours=3)
    return Clients.query.filter(Clients._date >= three_hours_ago)
