#!/usr/bin/env python3
# Soubor:  __init__.py
# Úloha:  Flask -- aplikace
############################################################################
from flask import Flask

app = Flask(__name__)
app.secret_key = b'U\xd4\xb1\xe4\x00\xceF\xdd\xd0\x0b\xe9'
'\xe6\x80\x92\x8b\x88\xaa*\x99\x02\xd6\xc0\xd8\x98'

from . import views
