# Task = input("Enter you task: ")
# Time_Bound = input("Is it time-bound (yes/no): ")
# Priority = input("Priority (high/medium/low): ")

# Reminder = f"'{Task}' is a {Priority} priority task "
# match Priority:
#     case "high":
#         Reminder += "that should be handled urgently "
#     case "medium":
#         Reminder += "that needs attention soon."
#     case "low":
#         Reminder += "that can be done at a convenient time."
#     case _:
#         Reminder = "Invalid priority level. please choose high, medium, or low."
# if Time_Bound == "yes" and Priority in {"high", "medium", "low"}:
#     Reminder += "It requires immediate attention today!"
# print(f"Reminder: {Reminder}")










Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ")


Reminder = f"'{Task}' is a {Priority} priority task "
match Priority:
    case "high":
        Reminder += "that should be handled urgently "
    case "medium":
        Reminder += "that needs attention soon."
    case "low":
        Reminder += "that can be done at a convenient time."
    case _:
        Reminder = "Invalid priority level. please choose high, medium, or low."
if Time_Bound == "yes" and Priority in {"high", "medium", "low"}:
    Reminder += "It requires immediate attention today!"
print(f"Reminder: {Reminder}")
