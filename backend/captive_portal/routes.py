from flask import render_template, request, session, redirect, url_for, flash, Blueprint
from backend.captive_portal.forms import RegistrationForm, AccessForm
from backend.constants import Constants as cts
from backend.captive_portal.check_input_errors import user_input_errors, check_if_same_client
from backend.captive_portal.database_operations import save_info_db


captive = Blueprint('captive', __name__)


@captive.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        lastname = form.lastname.data
        email = form.email.data
        movil = form.movil.data
        session["client_ip"] = request.args.get('client_ip')
        session["client_mac"] = request.args.get('client_mac')
        session["grant_url"] = request.args.get('base_grant_url')
        session["User-Agent"] = request.args.get('User-Agent')
        session["Node_mac"] = request.args.get('node_mac')
        session["user_continue_url"] = request.args.get('user_continue_url')

        print('User-Agent: ', session["User-Agent"])

        error = user_input_errors(name.replace(' ', ''), lastname.replace(' ', ''), email, movil)
        same_client = check_if_same_client(email.lower(), session["client_mac"])

        if not error and not same_client:
            save_info_db(
                name.lower(),
                lastname.lower(),
                email.lower(),
                movil,
                session["client_ip"],
                session["client_mac"],
                session["User-Agent"]
            )
            flash(f'Bienvenid@ {name} tu acceso a Internet ha sido habilitado, dispones de 1 hora, presiona continuar', 'success')
            return redirect(url_for('captive.welcome'))
        else:
            if same_client:
                flash(same_client, 'danger')
            else:
                flash(error, 'danger')

    return render_template("register.html", tittle='Register', form=form, company=cts.COMPANY_NAME)


@captive.route('/welcome', methods=['GET', 'POST'])
def welcome():
    form = AccessForm()
    if form.validate_on_submit():
       redirect_url = session["grant_url"] + "?continue=" + session["user_continue_url"]
       # redirect_url = 'https://www.google.com'
       return redirect(redirect_url, code=302)

    return render_template("welcome.html", tittle='welcome', form=form, company=cts.COMPANY_NAME)
