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

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
