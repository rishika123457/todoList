def main():
  # Initialize an empty list to store tasks
  tasks = []

  while True:
    # Display menu options
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Exit")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    # Handle user choices
    if choice == '1':
      # Add a new task
      task = input("Enter a new task: ")
      tasks.append(task)
      print(f"Task '{task}' added successfully!")
    elif choice == '2':
      # View all tasks
      if not tasks:
        print("No tasks added yet!")
      else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
    elif choice == '3':
      # Mark a task done
      if not tasks:
        print("No tasks to mark done!")
      else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        try:
          done_index = int(input("Enter the number of the task to mark done: ")) - 1
          tasks.pop(done_index)
          print("Task marked done successfully!")
        except (IndexError, ValueError):
          print("Invalid task number!")
    elif choice == '4':
      # Exit the program
      print("Exiting To-Do List App...")
      break
    else:
      # Handle invalid choices
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()
