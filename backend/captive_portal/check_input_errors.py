from pyisemail import is_email
from backend.captive_portal.database_operations import check_last_clients


def user_input_errors(name, lastname, email, movil):
    if not name.isalpha():
        return f'El campo nombre es incorrecto'

    if not lastname.isalpha():
        return f'El campo apellido es incorrecto'

    if not movil.startswith('09') or not movil.isdigit():
        return f'El numero de celular es incorrecto'

    if not email or not is_email(email, check_dns=True):
        return f'El campo email es incorrecto'

    return False


def check_if_same_client(email, mac):
    clients = check_last_clients()
    email_counter = [item.email for item in clients].count(email)
    mac_counter = [item.mac for item in clients].count(mac)

    if email_counter >= 2 or mac_counter >= 2:
        return '''Tu email o dispositivo ya han sido utilizados en las ultimas dos horas.
        Debes esperar una hora desde tu ultima desconexion para acceder nuevamente a internet!!'''

    return False
