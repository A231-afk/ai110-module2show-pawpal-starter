import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
st.session_state.owner.name = owner_name
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if st.button("Add pet"):
    pet = Pet(pet_name, species)
    st.session_state.owner.add_pet(pet)
    st.success(f"Added {pet_name}!")

if st.session_state.owner.pets:
    selected_pet = st.selectbox("Choose pet", st.session_state.owner.pets, format_func=lambda pet: pet.name)

    task_title = st.text_input("Task title", value="Morning walk")
    time_of_day = st.text_input("Time", value="07:00")
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        selected_pet.add_task(Task(task_title, time_of_day, priority, due_date="2026-07-08"))
        st.success(f"Added task to {selected_pet.name}")

    st.write("Current tasks:")
    for pet in st.session_state.owner.pets:
        for task in pet.tasks:
            st.write(f"{pet.name}: {task.time_of_day} — {task.description} ({task.priority})")
else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    schedule = scheduler.sort_tasks_by_time()

    if schedule:
        st.write("Today's Schedule:")
        for task in schedule:
            st.write(f"{task.time_of_day} — {task.description} ({task.priority})")
    else:
        st.info("No tasks to schedule yet.")