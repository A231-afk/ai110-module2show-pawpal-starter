"""Beginner-friendly pytest tests for pawpal_system.py."""

from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_mark_complete():
    # A new task should start as not completed
    task = Task("Morning walk", "07:00", "high", due_date="2026-07-08")
    assert task.completed is False

    # After marking complete, it should be True
    task.mark_complete()
    assert task.completed is True


def test_pet_add_task_increases_count():
    # A new pet starts with no tasks
    pet = Pet("Rex", "dog")
    initial_count = len(pet.tasks)

    # Adding a task should increase the count by one
    pet.add_task(Task("Feed breakfast", "08:00", "high", due_date="2026-07-08"))
    assert len(pet.tasks) == initial_count + 1


def test_scheduler_sorts_tasks_by_time():
    # Set up an owner with one pet and tasks added out of order
    owner = Owner("Amr")
    pet = Pet("Rex", "dog")
    owner.add_pet(pet)
    pet.add_task(Task("Evening walk", "17:00", "medium", due_date="2026-07-08"))
    pet.add_task(Task("Morning walk", "07:00", "high", due_date="2026-07-08"))

    # The scheduler should return them in time order
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_tasks_by_time()
    times = [task.time_of_day for task in sorted_tasks]
    assert times == ["07:00", "17:00"]


def test_completing_daily_task_creates_next_day_task():
    # Set up a pet with one daily recurring task
    owner = Owner("Amr")
    pet = Pet("Rex", "dog")
    owner.add_pet(pet)
    daily_task = Task("Morning walk", "07:00", "high", due_date="2026-07-08", frequency="daily")
    pet.add_task(daily_task)

    # Completing it should create a new task for the next day
    scheduler = Scheduler(owner)
    new_task = scheduler.complete_task(daily_task)
    assert new_task is not None
    assert new_task.due_date == "2026-07-09"
    assert new_task.completed is False


def test_detect_conflicts_finds_same_date_and_time():
    # Two tasks share the same due_date and time_of_day
    owner = Owner("Amr")
    pet = Pet("Rex", "dog")
    owner.add_pet(pet)
    pet.add_task(Task("Give medicine", "12:00", "high", due_date="2026-07-08"))
    pet.add_task(Task("Brush fur", "12:00", "low", due_date="2026-07-08"))

    # The scheduler should report one conflict warning
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) == 1
