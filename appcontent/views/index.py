# -*- coding: utf-8 -*-
__author__ = 'qi.zhang01'

from flask import Flask
from flask import Flask, redirect, url_for, render_template, request, Response
import os
from flask import Blueprint

index = Blueprint('index', __name__)


@index.route('/index', methods=['GET'])
def indexPage():
    return render_template("index.html")

@index.route('/forms', methods=["GET", 'POST'])
def forms():
    return render_template("forms.html")

@index.route('/tables', methods=["GET", 'POST'])
def tables():
    return render_template("tables.html")

@index.route('/components', methods=["GET", 'POST'])
def components():
    return render_template("components.html")
