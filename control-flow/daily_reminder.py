task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Reminder:{task} is a high priority task that requires immediate attention today!")

    case "medium":
        print(f"Reminder:{task} is a medium priority task.")

    case "low":
        Reminder = (f"{task} is a low priority task.")

    case _:
        Reminder = "f{task} has unknown priority level."

        if time_bound  == "yes":
            Reminder += "It requires immediate attention today!"

        else:
            Reminder += "Consider completing it when you have free time."
            print(f"\nReminder: {Reminder}")
            
