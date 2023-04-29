from weddingplanner import db


class Wedding(db.Model):
    # schema for the Wedding model
    id = db.Column(db.Integer, primary_key=True)
    wedding_name = db.Column(db.String(25), unique=True, nullable=False)
    wedding_date = db.Column(db.Date, nullable=False)
    wedding_town = db.Column(db.String(25), nullable=False)
    wedding_country = db.Column(db.String(25), nullable=False)
    # many tasks to one wedding relationship,
    #   if wedding is deleted so are associated tasks
    # lazy=True means all tasks are identified simulataneously
    #   on querying wedding
    tasks = db.relationship("Task", backref="wedding",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.wedding_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    task_completed = db.Column(db.Boolean, default=False, nullable=False)
    # one wedding to many tasks relationship,
    #   if wedding is deleted so are associated tasks
    wedding_id = db.Column(db.Integer, db.ForeignKey("wedding.id",
                           ondelete="CASCADE"), nullable=False)
    # many suppliers to one task relationship,
    #   if task is deleted so are associated suppliers
    # lazy=True means all suppliers are identified simulataneously
    #   on querying task
    suppliers = db.relationship("Supplier", backref="task",
                                cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )


class Supplier(db.Model):
    # schema for the Supplier model
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(25), unique=True, nullable=False)
    supplier_telephone = db.Column(db.Integer, nullable=False)
    supplier_email = db.Column(db.String(25), nullable=False)
    supplier_address = db.Column(db.Text, nullable=False)
    booked = db.Column(db.Boolean, default=False, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    deposit = db.Column(db.Float, nullable=False)
    deposit_paid = db.Column(db.Boolean, default=False, nullable=False)
    balance_due_date = db.Column(db.Date, nullable=False)
    balance_paid = db.Column(db.Boolean, default=False, nullable=False)
    # one task to many suppliers relationship,
    #   if task is deleted so are associated suppliers
    task_id = db.Column(db.Integer, db.ForeignKey("task.id",
                        ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Supplier: {1} | Booked: {2}".format(
            self.id, self.supplier_name, self.booked
        )
