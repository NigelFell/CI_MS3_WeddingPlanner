from flask import render_template, request, redirect, url_for
from weddingplanner import app, db
from weddingplanner.models import Wedding, Task, Supplier
from weddingplanner.deftaskdata import get_default_task_list
from datetime import date, timedelta

# global variables for search facility!
global_wedding_id = None
global_wedding_country = None
global_wedding_town = None


@app.route("/")
def home():
    """
        home() function for @app.route("/") page
        retrieves a list of weddings from the database by the global variables set
        and renders weddings.html with the passsed Wedding list
    """
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
    """
        search_weddings() function for @app.route("/search_weddings") form
        On GET:
            builds lists of sorted Weddings, countries and towns
            and renders search_weddings.html with the lists
        On POST:
            sets the global search variables
            and redirects to weddings.html
    """
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
    """
        add_wedding() function for @app.route("/add_wedding") form
        On GET:
            renders add_wedding.html passing error="None"
        On POST:
            retrieves a list of all weddings from the database and the new wedding name to be added
            if the wedding name is found in the list renders add_wedding.html passing error=error_message
            else creates a Wedding object with the form attributes
            saves the Wedding object to the database
            and redirects to weddings.html
    """
    if request.method == "POST":
        weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
        wedding_name = request.form.get("wedding_name")
        for wedding in weddings:
            if wedding.wedding_name == wedding_name:
                error_message = "Sorry, '" + wedding_name + "' is already being used!"
                return render_template("add_wedding.html", error=error_message)

        wedding = Wedding(
            wedding_name=wedding_name,
            wedding_date=request.form.get("wedding_date"),
            wedding_town=request.form.get("wedding_town"),
            wedding_country=request.form.get("wedding_country")
        )
        db.session.add(wedding)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("add_wedding.html", error="None")


@app.route("/edit_wedding/<int:wedding_id>", methods=["GET", "POST"])
def edit_wedding(wedding_id):
    """
        edit_wedding(wedding_id) function for @app.route("/edit_wedding/<int:wedding_id>") form
        On GET:
            retrieves a Wedding object from the database by wedding_id
            and renders edit_wedding.html with the passed Wedding object
        On POST:
            edits the Wedding object with the form attributes
            saves the Wedding object to the database
            and redirects to weddings.html
    """
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
    """
        delete_wedding(wedding_id) function for @app.route("/delete_wedding/<int:wedding_id>")
        retrieves a Wedding object from the database by wedding_id
        deletes the Wedding object from the database
        and redirects to weddings.html
    """
    wedding = Wedding.query.get_or_404(wedding_id)
    db.session.delete(wedding)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/tasks")
def tasks():
    """
        tasks() function for @app.route("/tasks") page
        retrieves a list of all tasks from the database
        and renders tasks.html with the passed Task list
    """
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    """
        add_task() function for @app.route("/add_task") form
        On GET:
            retrieves a list of all weddings from the database
            and renders add_task.html with the passed Wedding list
        On POST:
            creates a Task object with the form attributes
            saves the Task object to the database
            and redirects to tasks.html
    """
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
    """
        edit_task(task_id) function for @app.route("/edit_task/<int:task_id>") form
        On GET:
            retrieves a Task object from the database by task_id
            retrieves a list of all weddings from the database
            and renders edit_task.html with the passed Task object and Wedding list
        On POST:
            edits the Task object with the form attributes
            saves the Task object to the database
            and redirects to tasks.html
    """
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
    """
        delete_task(task_id) function for @app.route("/delete_task/<int:task_id>")
        retrieves a Task object from the database by task_id
        deletes the Task object from the database
        and redirects to tasks.html
    """
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))


@app.route("/wedding_tasks/<int:wedding_id>")
def wedding_tasks(wedding_id):
    """
        wedding_tasks(wedding_id) function for @app.route("/wedding_tasks/<int:wedding_id>") page
        retrieves the Wedding object and list of tasks by wedding_id from the database
        and renders wedding_tasks.html with the passed Wedding and Task list
    """
    wedding = Wedding.query.get_or_404(wedding_id)
    tasks = list(Task.query.filter_by(wedding_id=wedding_id))
    return render_template("wedding_tasks.html", wedding=wedding, tasks=tasks)


@app.route("/add_wedding_task/<int:wedding_id>", methods=["GET", "POST"])
def add_wedding_task(wedding_id):
    """
        add_wedding_task(wedding_id) function for @app.route("/add_wedding_task/<int:wedding_id>") form
        On GET:
            retrieves a Wedding from the database by wedding_id
            and renders add_wedding_task.html with the passed Wedding
        On POST:
            creates a Task object with the form attributes
            saves the Task object to the database
            and redirects to wedding_tasks.html with the passed wedding_id
    """
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


@app.route("/edit_wedding_task/<int:task_id>", methods=["GET", "POST"])
def edit_wedding_task(task_id):
    """
        edit_wedding_task(task_id) function for @app.route("/edit_wedding_task/<int:task_id>") form
        On GET:
            retrieves a Task object from the database by task_id
            retrieves a Wedding object from the database by task.wedding_id
            and renders edit_wedding_task.html with the passed Wedding and Task objects
        On POST:
            edits the Task object with the form attributes
            saves the Task object to the database
            and redirects to wedding_tasks.html with the passed wedding_id
    """
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


@app.route("/delete_wedding_task/<int:task_id>")
def delete_wedding_task(task_id):
    """
        delete_wedding_task(task_id) function
        retrieves a Task object from the database by task_id
        deletes the Task object from the database
        and redirects to wedding_tasks.html with the passed wedding_id
    """
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("wedding_tasks", wedding_id=task.wedding_id))


@app.route("/add_default_tasks/<int:wedding_id>")
def add_default_tasks(wedding_id):
    """
        add_default_tasks(wedding_id) function
        gets a list of default tasks with get_default_task_list(wedding_id)
        adds each Task to the database
        and redirects to wedding_tasks.html with the passed wedding_id
    """
    tasks = get_default_task_list(wedding_id)

    for task in tasks:
        db.session.add(task)

    db.session.commit()
    return redirect(url_for("wedding_tasks", wedding_id=wedding_id))


@app.route("/suppliers")
def suppliers():
    """
        suppliers() function for @app.route("/suppliers") page
        retrieves a list of all suppliers from the database
        and renders suppliers.html with the passed Suppliers list
    """
    suppliers = list(Supplier.query.order_by(Supplier.id).all())
    return render_template("suppliers.html", suppliers=suppliers)


@app.route("/add_supplier", methods=["GET", "POST"])
def add_supplier():
    """
        add_supplier() function for @app.route("/add_supplier") form
        On GET:
            retrieves a list of all tasks from the database
            and renders add_supplier.html with the passed Task list
        On POST:
            creates a Supplier object with the form attributes
            saves the Supplier object to the database
            and redirects to suppliers.html
    """
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
    """
        edit_supplier(v_id) function for @app.route("/edit_supplier/<int:supplier_id>") form
        On GET:
            retrieves a Supplier object from the database by supplier_id
            retrieves a list of all tasks from the database
            and renders edit_supplier.html with the passed Supplier object and Task list
        On POST:
            edits the Supplier object with the form attributes
            saves the Supplier object to the database
            and redirects to suppliers.html
    """
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
    """
        delete_supplier(supplier_id) function for @app.route("/delete_supplier/<int:supplier_id>")
        retrieves a Supplier object from the database by supplier_id
        deletes the Supplier object from the database
        and redirects to suppliers.html
    """
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for("suppliers"))


@app.route("/task_suppliers/<int:task_id>")
def task_suppliers(task_id):
    """
        task_suppliers(task_id) function for @app.route("/task_suppliers/<int:task_id>") page
        retrieves the Task object by task_id from the database
        retrieves the Wedding object by task.wedding_id from the database
        retrieves list of suppliers by task_id from the database
        and renders task_suppliers.html with the passed Wedding, Task and suppliers list
    """
    task = Task.query.get_or_404(task_id)
    wedding = Wedding.query.get_or_404(task.wedding_id)
    suppliers = list(Supplier.query.filter_by(task_id=task_id))
    return render_template("task_suppliers.html", wedding=wedding, task=task, suppliers=suppliers)


@app.route("/add_task_supplier/<int:task_id>", methods=["GET", "POST"])
def add_task_supplier(task_id):
    """
        add_task_supplier(task_id) function for @app.route("/add_task_supplier/<int:task_id>") form
        On GET:
            retrieves a Task from the database by task_id
            retrieves a Wedding from the database by task.wedding_id
            and renders add_task_supplier.html with the passed Wedding and Task objects
        On POST:
            creates a Supplier object with the form attributes
            saves the Supplier object to the database
            and redirects to task_suppliers.html with the passed task_id
    """
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


@app.route("/edit_task_supplier/<int:supplier_id>", methods=["GET", "POST"])
def edit_task_supplier(supplier_id):
    """
        edit_task_supplier(suppiier_id) function for @app.route("/edit_task_supplier/<int:supplier_id>") form
        On GET:
            retrieves a Supplier object from the database by supplier_id
            retrieves a Task object from the database by supplier.task_id
            retrieves a Wedding object from the database by task.wedding_id
            and renders edit_task_supplier.html with the passed Wedding, Task and Supplier objects
        On POST:
            edits the Supplier object with the form attributes
            saves the Supplier object to the database
            and redirects to task_suppliers.html with the passed supplier.task_id
    """
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
    """
        copy_task_supplier(suppiier_id) function for @app.route("/copy_task_supplier/<int:supplier_id>") form
        On GET:
            retrieves the Supplier object to copy from the database by supplier_id
            retrieves a list of all weddings from the database
            iterates through the wedding list creating a dictionary with 
                key:wedding_name and value:tasks list for the wedding
            and renders copy_task_supplier.html with the passed Supplier to copy and Wedding:Tasks list dictionary
        On POST:
            retrieves the Task objest (from the form attribute) that the Supplier will be copied to 
            creates a new Supplier object from the Supplier object to be copied
            saves the new Supplier object to the database
            and redirects to task_suppliers.html with the passed supplier.task_id
    """
    from_supplier = Supplier.query.get_or_404(supplier_id)

    if request.method == "POST":
        to_task = Task.query.get_or_404(request.form.get("task_id"))
        balance_due_date = to_task.due_date - timedelta(weeks=1)
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
    
    wedding_tasks = {}
    weddings = list(Wedding.query.order_by(Wedding.wedding_name).all())
    for wedding in weddings:
        tasks = list(Task.query.order_by(Task.task_name).filter_by(wedding_id=wedding.id))
        wedding_tasks.update({wedding.wedding_name: tasks})
    return render_template("copy_task_supplier.html", supplier=from_supplier, wedding_tasks=wedding_tasks)


@app.route("/delete_task_supplier/<int:supplier_id>")
def delete_task_supplier(supplier_id):
    """
        delete_task_supplier(supplier_id) function for @app.route("/delete_task_supplier/<int:supplier_id>")
        retrieves a Supplier object from the database by supplier_id
        deletes the Supplier object from the database
        and redirects to task_suppliers.html with the passed supplier.task_id
    """
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return redirect(url_for("task_suppliers", task_id=supplier.task_id))
