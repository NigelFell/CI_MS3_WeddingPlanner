from flask import render_template, request, redirect, url_for
from weddingplanner import app, db
from weddingplanner.models import Wedding, Task, Supplier


@app.route("/")
def home():
    return render_template("weddings.html")
