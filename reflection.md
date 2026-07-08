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
One tradeoff my scheduler makes is keeping the scheduling logic simple by sorting tasks with 24-hour time strings instead of using a more advanced date/time system. This is reasonable because the app is focused on a daily pet care plan, and times like `07:00`, `08:00`, and `17:00` sort correctly and are easy to understand.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---
## 4. Testing and Verification

**a. What you tested**

I tested that `mark_complete()` changes a task from incomplete to complete. I also tested that adding a task to a pet increases the pet’s task list by one. These tests are important because completion tracking and task storage are core behaviors used by the scheduler and UI.

**b. Confidence**

I am fairly confident that the basic scheduler works because the demo script runs successfully and the pytest tests pass. If I had more time, I would test more edge cases, such as multiple pets with tasks at the same time, pets with no tasks, and filtering completed tasks from the final schedule.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
