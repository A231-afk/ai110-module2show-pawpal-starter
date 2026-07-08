"""PawPal+ demo — show the Phase 4 smarter scheduling features."""

from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    # Create the owner and two pets
    owner = Owner("Amr")
    rex = Pet("Rex", "dog")
    mimi = Pet("Mimi", "cat")
    owner.add_pet(rex)
    owner.add_pet(mimi)

    # Add tasks out of chronological order, with valid due dates.
    # "Morning walk" is a daily recurring task (kept in a variable so we can complete it later).
    morning_walk = Task("Morning walk", "07:00", "high", due_date="2026-07-08", frequency="daily")
    rex.add_task(Task("Evening walk", "17:00", "medium", due_date="2026-07-08"))
    rex.add_task(morning_walk)
    mimi.add_task(Task("Feed breakfast", "08:00", "high", due_date="2026-07-08"))

    # Two tasks that share the same due_date and time_of_day -> a conflict.
    rex.add_task(Task("Give medicine", "12:00", "high", due_date="2026-07-08"))
    mimi.add_task(Task("Brush fur", "12:00", "low", due_date="2026-07-08"))

    scheduler = Scheduler(owner)

    # 1) Sorted schedule (notice the out-of-order tasks come out in time order)
    print("Today's Schedule (sorted by time)")
    print("---------------------------------")
    for task in scheduler.sort_tasks_by_time():
        print(f"{task.time_of_day}  {task.description} ({task.priority})")
    print()

    # 2) Tasks filtered by pet
    print("Tasks for Rex")
    print("-------------")
    for task in scheduler.filter_tasks_by_pet("Rex"):
        print(f"{task.time_of_day}  {task.description}")
    print()

    # 3) Complete the daily recurring task and show the new one that appears
    print("Completing the daily recurring task")
    print("-----------------------------------")
    new_task = scheduler.complete_task(morning_walk)
    print(f"Completed: {morning_walk.description} on {morning_walk.due_date}")
    if new_task is not None:
        print(f"Next one:  {new_task.description} on {new_task.due_date} (completed={new_task.completed})")
    print()

    # 4) Conflict warnings
    print("Conflict Check")
    print("--------------")
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()
