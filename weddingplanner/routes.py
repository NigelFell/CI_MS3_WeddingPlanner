from flask import render_template, request, redirect, url_for
from weddingplanner import app, db
from weddingplanner.models import Wedding, Task, Supplier
from weddingplanner.deftaskdata import get_default_task_list
from datetime import date, timedelta

global_wedding_id = None
global_wedding_country = None
global_wedding_town = None


@app.route("/")
def home():
    weddings = []
    if global_wedding_id is not None:
        weddings = list(Wedding.query.filter_by(id=global_wedding_id))
    elif global_wedding_country is None and global_wedding_town is None:
        weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    elif global_wedding_country is not None and global_wedding_town is None:
        weddings = list(Wedding.query.order_by(Wedding.wedding_name)
                        .filter_by(wedding_country=global_wedding_country))
    elif global_wedding_country is None and global_wedding_town is not None:
        weddings = list(Wedding.query.order_by(Wedding.wedding_name)
                        .filter_by(wedding_town=global_wedding_town))
    else:
        weddings = list(Wedding.query.order_by(Wedding.wedding_name)
                        .filter_by(wedding_country=global_wedding_country)
                        .filter_by(wedding_town=global_wedding_town))
        
    return render_template("weddings.html", weddings=weddings)


@app.route("/search_weddings", methods=["GET", "POST"])
def search_weddings():
    global global_wedding_id
    global global_wedding_country
    global global_wedding_town

    if request.method == "POST":
        global_wedding_id = request.form.get("wedding_id")
        global_wedding_country = request.form.get("wedding_country")
        global_wedding_town = request.form.get("wedding_town")
        return redirect(url_for("home"))

    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    countries_set = set()
    towns_set = set()
    for wedding in weddings:
        countries_set.add(wedding.wedding_country)
        towns_set.add(wedding.wedding_town)
    countries = list(countries_set)
    countries.sort()
    towns = list(towns_set)
    towns.sort()
    return render_template("search_weddings.html", weddings=weddings, countries=countries, towns=towns)


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


@app.route("/add_wedding_task/<int:wedding_id>", methods=["GET", "POST"])
def add_wedding_task(wedding_id):
    wedding = Wedding.query.get_or_404(wedding_id)
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            task_completed=bool(
                True if request.form.get("task_completed") else False),
            wedding_id=wedding_id
        )
        db.session.add(task)
        db.session.commit()

        return redirect(url_for("wedding_tasks", wedding_id=wedding_id))
    return render_template("add_wedding_task.html", wedding=wedding)


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


@app.route("/edit_wedding_task/<int:task_id>", methods=["GET", "POST"])
def edit_wedding_task(task_id):
    task = Task.query.get_or_404(task_id)
    wedding = Wedding.query.get_or_404(task.wedding_id)
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.task_completed = bool(
            True if request.form.get("task_completed") else False)
        db.session.commit()
        return redirect(url_for("wedding_tasks", wedding_id=task.wedding_id))
    return render_template("edit_wedding_task.html", wedding=wedding, task=task)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))


@app.route("/delete_wedding_task/<int:task_id>")
def delete_wedding_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("wedding_tasks", wedding_id=task.wedding_id))


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


@app.route("/add_task_supplier/<int:task_id>", methods=["GET", "POST"])
def add_task_supplier(task_id):
    task = Task.query.get_or_404(task_id)
    wedding = Wedding.query.get_or_404(task.wedding_id)
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
            task_id=task_id
        )
        db.session.add(supplier)
        db.session.commit()

        return redirect(url_for("task_suppliers", task_id=task_id))
    return render_template("add_task_supplier.html", wedding=wedding, task=task)


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


@app.route("/edit_task_supplier/<int:supplier_id>", methods=["GET", "POST"])
def edit_task_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    task = Task.query.get_or_404(supplier.task_id)
    wedding = Wedding.query.get_or_404(task.wedding_id)
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
        db.session.commit()
        return redirect(url_for("task_suppliers", task_id=supplier.task_id))
    return render_template(
        "edit_task_supplier.html", wedding=wedding, task=task, supplier=supplier)


@app.route("/copy_task_supplier/<int:supplier_id>", methods=["GET", "POST"])
def copy_task_supplier(supplier_id):
    from_supplier = Supplier.query.get_or_404(supplier_id)

    if request.method == "POST":
        to_task = Task.query.get_or_404(request.form.get("task_id"))
        balance_due_date = to_task.due_date - timedelta(weeks = 1)
        supplier = Supplier(
            supplier_name=from_supplier.supplier_name,
            supplier_telephone=from_supplier.supplier_telephone,
            supplier_email=from_supplier.supplier_email,
            supplier_address=from_supplier.supplier_address,
            supplier_description=from_supplier.supplier_description,
            booked=bool(False),
            cost=from_supplier.cost,
            deposit=from_supplier.deposit,
            deposit_paid=bool(False),
            balance_due_date=balance_due_date,
            balance_paid=bool(False),
            task_id=request.form.get("task_id")
        )
        db.session.add(supplier)
        db.session.commit()
        return redirect(url_for("task_suppliers", task_id=supplier.task_id))
    
    # weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    # tasks = list(Task.query.order_by(Task.task_name).all())

    wedding_tasks = {}
    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    for wedding in weddings:
        tasks = list(Task.query.order_by(Task.task_name).filter_by(wedding_id=wedding.id))
        wedding_tasks.update({wedding.wedding_name: tasks})
    return render_template("copy_task_supplier.html", supplier=from_supplier, wedding_tasks=wedding_tasks)


@app.route("/delete_supplier/<int:supplier_id>")
def delete_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for("suppliers"))


@app.route("/delete_task_supplier/<int:supplier_id>")
def delete_task_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for("task_suppliers", task_id=supplier.task_id))
