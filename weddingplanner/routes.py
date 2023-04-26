from flask import render_template, request, redirect, url_for
from weddingplanner import app, db
from weddingplanner.models import Wedding, Task, Supplier


@app.route("/")
def home():
    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    return render_template("weddings.html", weddings=weddings)


@app.route("/add_wedding", methods=["GET", "POST"])
def add_wedding():
    if request.method == "POST":
        wedding = Wedding(
            wedding_name=request.form.get("wedding_name"),
            wedding_date=request.form.get("wedding_date"),
            wedding_town=request.form.get("wedding_town"),
            wedding_country=request.form.get("wedding_country")
        )
        db.session.add(wedding)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_wedding.html")


@app.route("/edit_wedding/<int:wedding_id>", methods=["GET", "POST"])
def edit_wedding(wedding_id):
    wedding = Wedding.query.get_or_404(wedding_id)
    if request.method == "POST":
        wedding.wedding_name = request.form.get("wedding_name")
        wedding.wedding_date = request.form.get("wedding_date")
        wedding.wedding_town = request.form.get("wedding_town")
        wedding.wedding_country = request.form.get("wedding_country")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_wedding.html", wedding=wedding)


@app.route("/delete_wedding/<int:wedding_id>")
def delete_wedding(wedding_id):
    wedding = Wedding.query.get_or_404(wedding_id)
    db.session.delete(wedding)
    db.session.commit()
    return redirect(url_for("home"))
