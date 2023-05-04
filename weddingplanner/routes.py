from flask import render_template, request, redirect, url_for
from weddingplanner import app, db
from weddingplanner.models import Wedding, Task, Supplier
from weddingplanner.deftaskdata import get_default_task_list


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


@app.route("/tasks")
def tasks():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            task_completed=bool(
                True if request.form.get("task_completed") else False),
            wedding_id=request.form.get("wedding_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("tasks"))
    return render_template("add_task.html", weddings=weddings)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.task_completed = bool(
            True if request.form.get("task_completed") else False)
        task.wedding_id = request.form.get("wedding_id")
        db.session.commit()
        return redirect(url_for("tasks"))
    return render_template("edit_task.html", task=task, weddings=weddings)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))


@app.route("/add_default_tasks/<int:wedding_id>")
def add_default_tasks(wedding_id):
    tasks = get_default_task_list(wedding_id)

    for task in tasks:
        db.session.add(task)

    db.session.commit()
    return redirect(url_for("home"))


@app.route("/wedding_tasks/<int:wedding_id>")
def wedding_tasks(wedding_id):
    wedding = Wedding.query.get_or_404(wedding_id)
    tasks = list(Task.query.filter_by(wedding_id=wedding_id))
    return render_template("wedding_tasks.html", wedding=wedding, tasks=tasks)


@app.route("/task_suppliers/<int:task_id>")
def task_suppliers(task_id):
    task = Task.query.get_or_404(task_id)
    wedding = Wedding.query.get_or_404(task.wedding_id)
    suppliers = list(Supplier.query.filter_by(task_id=task_id))
    return render_template("task_suppliers.html", wedding=wedding, task=task, suppliers=suppliers)


@app.route("/suppliers")
def suppliers():
    suppliers = list(Supplier.query.order_by(Supplier.id).all())
    return render_template("suppliers.html", suppliers=suppliers)


@app.route("/add_supplier", methods=["GET", "POST"])
def add_supplier():
    tasks = list(Task.query.order_by(Task.task_name).all())
    if request.method == "POST":
        supplier = Supplier(
            supplier_name=request.form.get("supplier_name"),
            supplier_telephone=request.form.get("supplier_telephone"),
            supplier_email=request.form.get("supplier_email"),
            supplier_address=request.form.get("supplier_address"),
            supplier_description=request.form.get("supplier_description"),
            booked=bool(True if request.form.get("booked") else False),
            cost=request.form.get("cost"),
            deposit=request.form.get("deposit"),
            deposit_paid=bool(
                True if request.form.get("deposit_paid") else False),
            balance_due_date=request.form.get("balance_due_date"),
            balance_paid=bool(
                True if request.form.get("balance_paid") else False),
            task_id=request.form.get("task_id")
        )
        db.session.add(supplier)
        db.session.commit()
        return redirect(url_for("suppliers"))
    return render_template("add_supplier.html", tasks=tasks)


@app.route("/edit_supplier/<int:supplier_id>", methods=["GET", "POST"])
def edit_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    tasks = list(Task.query.order_by(Task.task_name).all())
    if request.method == "POST":
        supplier.supplier_name = request.form.get("supplier_name")
        supplier.supplier_telephone = request.form.get("supplier_telephone")
        supplier.supplier_email = request.form.get("supplier_email")
        supplier.supplier_address = request.form.get("supplier_address")
        supplier.supplier_description = request.form.get(
            "supplier_description")
        supplier.booked = bool(True if request.form.get("booked") else False)
        supplier.cost = request.form.get("cost")
        supplier.deposit = request.form.get("deposit")
        supplier.deposit_paid = bool(
            True if request.form.get("deposit_paid") else False)
        supplier.balance_due_date = request.form.get("balance_due_date")
        supplier.balance_paid = bool(
            True if request.form.get("balance_paid") else False)
        supplier.task_id = request.form.get("task_id")
        db.session.commit()
        return redirect(url_for("suppliers"))
    return render_template(
        "edit_supplier.html", supplier=supplier, tasks=tasks)


@app.route("/delete_supplier/<int:supplier_id>")
def delete_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for("suppliers"))
