# -*- coding: utf-8 -*-
"""
@author: Destroyers
@file: run.py
@time: 2018年6月21日 05:26:14
"""


from app import app
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Taffy Python3.x'
app.run(debug=True)