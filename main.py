"""PawPal+ demo — build a small schedule and print it in time order."""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # Create the owner
    owner = Owner("Amr")

    # Create two pets
    rex = Pet("Rex", "dog")
    mimi = Pet("Mimi", "cat")

    # Add both pets to the owner
    owner.add_pet(rex)
    owner.add_pet(mimi)

    # Create tasks across the two pets (24-hour time strings)
    rex.add_task(Task("Morning walk", "07:00", "high"))
    rex.add_task(Task("Evening walk", "17:00", "medium"))
    mimi.add_task(Task("Feed breakfast", "08:00", "high"))

    # Use the scheduler to sort all tasks by time
    scheduler = Scheduler(owner)
    tasks = scheduler.sort_tasks_by_time()

    # Print a readable schedule
    print("Today's Schedule")
    print("----------------")
    for task in tasks:
        print(f"{task.time_of_day}  {task.description} ({task.priority})")


if __name__ == "__main__":
    main()
