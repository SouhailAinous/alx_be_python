task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task and should be completed today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Schedule it for this week.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority but time-sensitive task. Try to do it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
