# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, Response
import os
from appcontent.com.Path import GetPath
from appcontent.com.Log import Getlog
from appcontent.views.login import login
from appcontent.views.index import index
from appcontent import services

app = Flask(__name__)

class Main():

    def __init__(self):
        self.app = app
        self.runPath = GetPath().getCurrentPath()
        #self.logger = Getlog(app, "1").startLog()

    def add_views_path(self):
        self.app.register_blueprint(login, url_prefix='/')
        self.app.register_blueprint(index, url_prefix='/')


if __name__ == '__main__':

    main = Main()
    main.add_views_path()
    main.app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)