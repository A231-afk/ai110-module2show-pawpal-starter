"""PawPal+ — class skeletons.

Structure derived from diagrams/uml.mmd. Method bodies are stubs;
scheduling logic is intentionally left unimplemented for this phase.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    description: str
    time_of_day: str
    priority: str
    due_date: str  # YYYY-MM-DD
    completed: bool = False
    frequency: str = "once"

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def show_tasks(self) -> list[Task]:
        """Return the pet's tasks."""
        return self.tasks


class Owner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner."""
        self.pets.remove(pet)

    def list_pets(self) -> list[Pet]:
        """Return the owner's pets."""
        return self.pets


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all of the owner's pets."""
        all_tasks = []
        for pet in self.owner.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def sort_tasks_by_time(self) -> list[Task]:
        """Return all tasks sorted by time of day."""
        return sorted(self.get_all_tasks(), key=lambda task: task.time_of_day)

    def get_incomplete_tasks(self) -> list[Task]:
        """Return all tasks that are not yet completed."""
        return [task for task in self.get_all_tasks() if not task.completed]

    def filter_tasks_by_pet(self, pet_name: str) -> list[Task]:
        """Return the tasks of the pet matching pet_name, or [] if none matches."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return pet.tasks
        return []

    def complete_task(self, task: Task) -> Task | None:
        """Complete a task and, if it recurs, schedule the next one on the same pet."""
        task.mark_complete()

        # A one-time task does not repeat.
        if task.frequency == "once":
            return None

        # Figure out how many days until the next occurrence.
        if task.frequency == "daily":
            days_ahead = 1
        elif task.frequency == "weekly":
            days_ahead = 7
        else:
            # Unknown frequency: treat it like a one-time task.
            return None

        # Calculate the next due date from the current one.
        current_date = datetime.strptime(task.due_date, "%Y-%m-%d")
        next_date = current_date + timedelta(days=days_ahead)
        next_due_date = next_date.strftime("%Y-%m-%d")

        # Build the next task, keeping the same details but not yet completed.
        new_task = Task(
            description=task.description,
            time_of_day=task.time_of_day,
            priority=task.priority,
            due_date=next_due_date,
            completed=False,
            frequency=task.frequency,
        )

        # Add the new task to whichever pet owned the original task.
        for pet in self.owner.pets:
            if task in pet.tasks:
                pet.add_task(new_task)
                break

        return new_task

    def detect_conflicts(self) -> list[str]:
        """Return a warning for each pair of tasks sharing a due_date and time_of_day."""
        warnings = []
        tasks = self.get_all_tasks()

        # Compare each task with every task after it, so each pair is checked once.
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                first = tasks[i]
                second = tasks[j]
                same_date = first.due_date == second.due_date
                same_time = first.time_of_day == second.time_of_day
                if same_date and same_time:
                    warnings.append(
                        f"Conflict: '{first.description}' and '{second.description}' "
                        f"are both scheduled on {first.due_date} at {first.time_of_day}."
                    )

        return warnings
