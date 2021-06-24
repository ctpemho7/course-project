# -*- coding: utf-8 -*-
from flask import Flask
import logging, os
import config

userApp = Flask(__name__)
# Load the views
from userApp.interfaces import *
# Load the config file
userApp.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
from userApp.helper import jinjaHelper

userApp.config.from_object('config')
userApp.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

logging.basicConfig(level = logging.INFO)