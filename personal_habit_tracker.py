
print("==============================")
print("      PERSONAL HABIT TRACKER")
print("==============================")

habits = [
    "Study Python",
    "Drink Water",
    "Exercise",
    "Read a Book",
    "Sleep on Time"
]

completed = []

def show_habits():
    print("\nYOUR DAILY HABITS")
    print("------------------------------")

    for i, habit in enumerate(habits):
        if habit in completed:
            print(i + 1, ".", habit, "- Completed")
        else:
            print(i + 1, ".", habit, "- Not Completed")

def mark_habit():
    show_habits()

    choice = int(input("\nEnter habit number: "))

    if choice >= 1 and choice <= len(habits):
        habit = habits[choice - 1]

        if habit not in completed:
            completed.append(habit)
            print("\nGreat!", habit, "completed!")
        else:
            print("\nYou already completed this habit!")
    else:
        print("\nInvalid habit number!")

def show_progress():
    total = len(habits)
    done = len(completed)
    remaining = total - done

    print("\n==============================")
    print("       DAILY PROGRESS")
    print("==============================")
    print("Total Habits:", total)
    print("Completed:", done)
    print("Remaining:", remaining)

    percentage = (done / total) * 100
    print("Progress:", round(percentage, 2), "%")

    if done == total:
        print("Amazing! All habits completed!")
    elif done >= 3:
        print("Great work! Keep going!")
    else:
        print("Keep working on your habits!")

while True:
    print("\n========== MENU ==========")
    print("1. View Habits")
    print("2. Complete a Habit")
    print("3. View Progress")
    print("4. Exit")

    option = input("\nEnter your choice: ")

    if option == "1":
        show_habits()

    elif option == "2":
        mark_habit()

    elif option == "3":
        show_progress()

    elif option == "4":
        print("\nThank you for using Habit Tracker!")
        break

    else:
        print("\nInvalid choice! Try again.")
