from flask import render_template, request, session, redirect, url_for, flash, request, Blueprint
from backend.admin.forms import LoginForm
from backend.constants import Constants as cts
from backend.admin.database_operations import login_process, clients_data
from flask_login import login_user, logout_user, login_required


admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = login_process(form.username.data, form.password.data)
        if user:
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.adminpage'))
        else:
            flash('Login Unsuccessful. Please check you username and password', 'danger')
    return render_template("login.html", tittle='Login', form=form, company=cts.COMPANY_NAME)


@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/adminpage')
@login_required
def adminpage():
    users = clients_data()
    return render_template("adminpage.html", tittle='Admin', title=cts.COMPANY_NAME, users=users)
