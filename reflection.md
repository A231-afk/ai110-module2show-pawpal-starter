# PawPal+ Project Reflection

## 1. System Design
Add basic owner and pet information.
Add care tasks for a pet, like feeding, walking, meds, or grooming.
Generate a daily schedule that orders tasks by priority and time.
**a. Initial design**

- Briefly describe your initial UML design. 
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class stores the owner's name and manages a list of pets. The Pet class stores identifying information such as the pet's name and species and manages that pet's tasks. The Task class represents an individual pet care activity and stores its description, time of day, priority, and completion status. The Scheduler class acts as the main scheduling component by retrieving tasks across all of the owner's pets, sorting them by time, and filtering out completed tasks. I designed the relationships so that one Owner can have multiple Pets, each Pet can have multiple Tasks, and the Scheduler uses the Owner to access tasks across all pets.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
At this stage, I have not made any major changes to my initial design. After reviewing the class skeleton, the relationships and responsibilities still appear appropriate for the current project requirements. I may revise the design later during implementation if I discover missing relationships or logic bottlenecks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
My scheduler considers task time, priority, and completion status. The main constraint is time because the daily plan should appear in chronological order. Priority is stored so the user can see which tasks matter most, and completion status is used to filter out tasks that are already done.
**b. Tradeoffs**
One tradeoff my scheduler makes is that conflict detection only checks for exact matches in due date and time. For example, two tasks scheduled at 08:00 on the same date are flagged as a conflict, but tasks at 08:00 and 08:05 are not considered overlapping. This keeps the algorithm simple and readable, but it does not account for task duration or partial overlaps. I decided this was reasonable for the current project because tasks do not yet store detailed start and end times.
---

## 3. AI Collaboration

**a. How you used AI**

I used AI throughout the whole project, but I tried to stay in charge of the decisions instead of just copying whatever it gave me. I started by having it help me turn my ideas into a Mermaid UML class diagram, which made it easy to see my four classes and their relationships before I wrote any code. Once I was happy with the diagram, I asked AI to turn the UML into Python class skeletons with just the attributes and method stubs, no logic yet. That kept the structure clean and matched my diagram.

After the skeletons were in place, I used AI to help me implement the method bodies one step at a time, like `mark_complete()`, the `add_pet`/`add_task` methods, and the harder Scheduler methods for recurring tasks and conflict detection. The most helpful prompts were specific ones where I described exactly what a method should do and what it should return, instead of asking for the whole project at once. AI was also really useful for debugging. For example, when my Streamlit tasks were not saving, it helped me figure out that the selectbox was returning a copy of the Pet object instead of the real one in session state. Finally, I used AI to write the pytest tests for my main behaviors so I could confirm everything worked.

**b. Judgment and verification**

One moment where I did not accept an AI suggestion as-is was around how to store the time of day for tasks. At first the idea was to use words like "morning" and "evening," but I realized that sorting those alphabetically would put "evening" before "morning," which is wrong. I changed the design to use 24-hour time strings like "07:00" and "17:00" instead, because those sort correctly as plain text and are clearer for the user. I verified my changes by running `main.py` and checking that the schedule actually came out in the right order, and by running `python3 -m pytest` to make sure all five tests still passed. I also tested the Streamlit app in the browser to confirm the fixes worked in the real UI, not just in theory.

---
## 4. Testing and Verification

**a. What you tested**

I tested that `mark_complete()` changes a task from incomplete to complete. I also tested that adding a task to a pet increases the pet’s task list by one. These tests are important because completion tracking and task storage are core behaviors used by the scheduler and UI.

**b. Confidence**

I have a high level of confidence in the core system because all five automated tests pass. The tests cover basic task management as well as the main scheduling algorithms, including sorting, recurrence, and conflict detection.
---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is the Scheduler class and how its smart features came together. Sorting, filtering by pet, recurring tasks, and conflict detection all work, and I have tests that prove it. I also liked how using separate chats for different parts of the project helped me stay organized. I kept one chat focused on the system design and UML, another for building and implementing the algorithms, and another for writing the tests. That way each conversation stayed on topic and I did not get confused by mixing design questions with debugging or testing questions. It felt like having separate notebooks for different parts of the same project.

**b. What you would improve**

If I had another iteration, I would improve conflict detection so it could handle task durations and partial overlaps, not just exact matches on date and time. I would also add a real date picker and frequency dropdown in the Streamlit UI instead of typing the due date by hand, so recurring tasks could be created directly from the app.

**c. Key takeaway**

The biggest thing I learned is what it means to be the lead architect while using AI. AI was great at generating code quickly, but it did not know my project goals or catch design problems like the morning/evening sorting issue. I had to make the real decisions, like how to structure my classes, what each method should return, and when a suggestion did not actually fit. I also had to verify everything by running the app and the tests instead of trusting the code just because it looked correct. AI worked best as a fast assistant, but I was the one responsible for the design and for making sure the final system actually worked.
