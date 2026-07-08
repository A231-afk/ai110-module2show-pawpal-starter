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
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        pass

    def show_tasks(self) -> list[Task]:
        """Return the pet's tasks."""
        pass


class Owner:
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner."""
        pass

    def list_pets(self) -> list[Pet]:
        """Return the owner's pets."""
        pass


class Scheduler:
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all of the owner's pets."""
        pass

    def sort_tasks_by_time(self) -> list[Task]:
        """Return all tasks sorted by time of day."""
        pass

    def get_incomplete_tasks(self) -> list[Task]:
        """Return all tasks that are not yet completed."""
        pass
