# -*- coding: utf-8 -*-
from flask import render_template, jsonify
from userApp import *

@userApp.route('/')
def index():
    return render_template('index.pug')


@userApp.route('/get_hello_world')
def hello_js():
    print('qwrqwr')
    return jsonify(text='Hello World!')