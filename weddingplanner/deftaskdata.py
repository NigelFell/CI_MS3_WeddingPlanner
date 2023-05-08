from weddingplanner.models import Task
from datetime import date, timedelta
import calendar


def get_default_task_list(wedding_id):
    today = date.today()
    tasks = []

    days_in_month = calendar.monthrange(today.year, today.month)[1]
    date_next_month = today + timedelta(days=days_in_month)
    task = Task(
        task_name="Book Church",
        task_description="Decide on location and book appointment with vicar",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    days_in_month = calendar.monthrange(date_next_month.year, date_next_month.month)[1]
    date_next_month = date_next_month + timedelta(days=days_in_month)
    task = Task(
        task_name="Book Party Venue",
        task_description="Decide on venue and book menu and drinks",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Notify/Book Registrars",
        task_description="Find and notify or book local registrars",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Book Honneymoon",
        task_description="Decide on where and book trip",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    days_in_month = calendar.monthrange(date_next_month.year, date_next_month.month)[1]
    date_next_month = date_next_month + timedelta(days=days_in_month)
    task = Task(
        task_name="Send Invites",
        task_description="Invite guests, bridesmaids, maid of honour and best man",
        is_urgent=bool(False),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    days_in_month = calendar.monthrange(date_next_month.year, date_next_month.month)[1]
    date_next_month = date_next_month + timedelta(days=days_in_month)
    task = Task(
        task_name="Get Wedding Dress",
        task_description="Find wedding dress and book alterations if necessary",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Get Other Dresses/Suits",
        task_description="Find bridesmaid/maid of honour dresses, suits and book alterations if necessary",
        is_urgent=bool(False),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Book Disco/Band",
        task_description="Find suitable disco or band for the wedding venue",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Book Photographer",
        task_description="Find photographer and organise times",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    task = Task(
        task_name="Book Florist",
        task_description="Find florist and organise what is required",
        is_urgent=bool(True),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    days_in_month = calendar.monthrange(date_next_month.year, date_next_month.month)[1]
    date_next_month = date_next_month + timedelta(days=days_in_month)
    task = Task(
        task_name="Order Cake",
        task_description="Order big enough cake for the number of guests",
        is_urgent=bool(False),
        due_date=date_next_month,
        task_completed=bool(False),
        wedding_id=wedding_id
    )
    tasks.append(task)

    return tasks
