from flask import render_template, request, redirect, url_for
from weddingplanner import app, db


@app.route("/")
def home():
    return render_template("base.html")
