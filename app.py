from flask import Flask
from flask import render_template
from flask import request,redirect,url_for
import sqlite3

app = Flask(__name__)

#renders homepage
@app.route("/")
def homePage():
    #calls homepage templates
    return render_template("homepage.html")

#info page
@app.route('/information')
def infoPage():
    return render_template("infoPage.html")

#page to view projects
@app.route('/projects')
def projects():
    return render_template("projects.html")

#to run flask app python -m flask run 
