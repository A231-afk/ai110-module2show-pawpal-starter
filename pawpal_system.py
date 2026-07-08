"""PawPal+ — class skeletons.

Structure derived from diagrams/uml.mmd. Method bodies are stubs;
scheduling logic is intentionally left unimplemented for this phase.
"""

from dataclasses import dataclass, field


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
