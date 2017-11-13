#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, request, flash,
                   redirect, session, url_for)
from webface import app
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login_post():
    jmeno = request.form.get('jmeno')
    heslo = request.form.get('heslo')
    print(jmeno, heslo)
    if jmeno == 'marek' and heslo == 'fixa':
        session['jmeno'] = jmeno
        flash('Úspěšně jsi se přihlásil.', 'zelena')
        return redirect(url_for('index'))
    else:
        flash('chybné jméno nebo heslo', 'cervena')
        return redirect(url_for('login'))


@app.route('/logout/', methods=['GET'])
def logout():
    session.pop('jmeno', None)
    return redirect(url_for('login'))


@app.route('/number/<i>')
def number(i):
    return render_template('number.html', number=i)


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404
