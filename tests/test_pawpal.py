"""Beginner-friendly pytest tests for pawpal_system.py."""

from pawpal_system import Task, Pet


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
