# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## ✨ Features

PawPal+ has four "smart scheduling" features, all handled by the `Scheduler` class:

| Feature | Method | What it does |
|---------|--------|--------------|
| **Sort by time** | `Scheduler.sort_tasks_by_time()` | Gathers every task across all pets and returns them in chronological order using 24-hour `HH:MM` time strings. |
| **Filter by pet** | `Scheduler.filter_tasks_by_pet(pet_name)` | Finds a pet by name and returns only that pet's tasks (empty list if the pet has none or doesn't exist). |
| **Recurring tasks** | `Scheduler.complete_task(task)` | Marks a task complete and, if it repeats `daily` or `weekly`, automatically creates the next task with an updated due date. |
| **Conflict detection** | `Scheduler.detect_conflicts()` | Returns warning messages whenever two tasks share the same due date and time of day. |

There is also `Scheduler.get_incomplete_tasks()` for listing tasks that still need to be done.

## 📸 Demo Walkthrough

You can follow along using the Streamlit app (`streamlit run app.py`):

1. **Add a pet** — Enter a pet name and species, then click **Add pet**. The pet is stored on the owner in session state.
2. **Add a task** — Choose the pet from the dropdown, then enter a task title, due date, time (in 24-hour `HH:MM` format), and priority. Click **Add task** and it appears under **Current tasks**.
3. **Generate the sorted schedule** — Click **Generate schedule**. The app calls `Scheduler.sort_tasks_by_time()` and shows all tasks in a clean table, ordered from earliest to latest.
4. **See conflict warnings** — The app also runs `Scheduler.detect_conflicts()`. If two tasks land on the same date and time, it shows a yellow `st.warning()` for each conflict. If everything is clear, it shows a green "No scheduling conflicts detected." message.

## 🖥️ Sample Output

Running the command-line demo shows all four features:

```bash
python3 main.py
```

```
Today's Schedule (sorted by time)
---------------------------------
07:00  Morning walk (high)
08:00  Feed breakfast (high)
12:00  Give medicine (high)
12:00  Brush fur (low)
17:00  Evening walk (medium)

Tasks for Rex
-------------
17:00  Evening walk
07:00  Morning walk
12:00  Give medicine

Completing the daily recurring task
-----------------------------------
Completed: Morning walk on 2026-07-08
Next one:  Morning walk on 2026-07-09 (completed=False)

Conflict Check
--------------
Conflict: 'Give medicine' and 'Brush fur' are both scheduled on 2026-07-08 at 12:00.
```

## 🧪 Testing

Run the full automated test suite with:

```bash
python3 -m pytest
```

Sample output:

```
collected 5 items

tests/test_pawpal.py .....                                               [100%]

============================== 5 passed in 0.04s ===============================
```

The five tests cover task completion, adding a task to a pet, sorting by time, daily recurring tasks, and conflict detection.
