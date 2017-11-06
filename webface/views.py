#!/usr/bin/env python3
# Soubor: views.py
# Úloha:  Flask --- pohledy
############################################################################
from flask import (render_template, Markup, request,
                   redirect, session)
from webface import app
############################################################################


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    jmeno = request.form.get('jmeno')
    heslo = request.form.get('heslo')
    print(jmeno, heslo)
    return render_template('login.html')


@app.route('/number/<i>')
def number(i):
    return render_template('number.html', number=i)


@app.errorhandler(404)
def page_not_found(error):
    print(error.code)
    print(error.name)
    print(error.description)
    return render_template('404.html', e=error), 404
