#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, request, flash,
                   redirect, session, url_for)
from werkzeug.security import check_password_hash
from webface import app
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


pwhash = {}
pwhash['marek'] = 'pbkdf2:sha1:1000$XQdCKTo3$3deeb4dc4c670b48f6183d4884ca99cda534294c'
pwhash['tonda'] = 'pbkdf2:sha1:1000$aBDfFHU2$2ae95982c428af53851fe5d0205e8f5623bd10ab'
pwhash['katka'] = 'pbkdf2:sha1:1000$2zq2mD5B$66bcce17e76eb41597432d8d603f7cdd6b460043'


@app.route('/login/', methods=['POST'])
def login_post():
    jmeno = request.form.get('jmeno')
    heslo = request.form.get('heslo')
    print(jmeno, heslo)
    if check_password_hash(str(pwhash.get(jmeno)), heslo):
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


@app.route('/tajne/')
def tajne():
    if 'jmeno' in session:
        return render_template('tajne.html')
    else:
        flash('Tato stránka je jen pro přihlášené.', 'oranzova')
        return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404
