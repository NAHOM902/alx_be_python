Task = input("Enter you task: ")
Priority = input("Priority (high/medium/low): ").lower()
Time_bound = input("Is it time-bound (yes/no): ").lower()

reminder = f"'{task}' is a {priority} priority task"
match priority:
    case "high":
        reminder += "that should be handled urgently"
    case "medium":
        reminder += "that needs attention soon."
    case "low":
        reminder += "that can be done at a convenient time."
    case _:
        reminder = "Invalid priority level. please choose high, medium, or low."
if time_bound == "yes" and priority in {"high", "medium", "low"}:
    reminder += "It requires immediate attention today!"
print(f"Reminder: {reminder}")