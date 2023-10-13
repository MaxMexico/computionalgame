# A simple Notes and Tasks Manager program
# This program allows users to create and manage notes and tasks with features like adding, displaying, marking as completed, and more.
#By MaxMexico

# Function to create a new note
"""
    Input: 
        - 'notes': A list to store notes.
        - 'category': The category of the note.
        - 'content': The content of the note.
    Process:
        - Creates a new note as a tuple with the provided category and content.
        - Appends the newly created note to the 'notes' list.
    Output:
        - Prints a confirmation message indicating that the note has been added in the specified category.
    """
def create_note(notes, category, content):
    # Create a tuple representing a note
    note = (category, content)
    notes.append(note)
    print(f"Note added in the '{category}' category.")

# Function to display notes by category

    """
    Input:
        - 'notes': A list containing stored notes.
    Process:
        - Checks if there are notes in the 'notes' list.
        - If there are no notes, it prints a message indicating that no notes have been recorded.
        - If there are notes, it displays each note's category and content along with an index.
        - Allows the user to select and display a specific note by index.
    Output:
        - Prints the list of notes and, if requested, a specific selected note.
    """

def display_notes(notes):
    if not notes:
        print("No notes recorded.")
        return
    
    print("Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. Category: {note[0]}, Content: {note[1]}")
    
    selected_index = int(input("Enter the index of the note you want to display: "))
    
    if 1 <= selected_index <= len(notes):
        selected_note = notes[selected_index - 1]
        print(f"Selected note - Category: {selected_note[0]}, Content: {selected_note[1]}")
    else:
        print("Invalid note index.")


# Function to add a task to the list

    """
    Input:
        - 'tasks': A list to store tasks.
        - 'task_description': The description of the task.
        - 'completed': A boolean indicating whether the task is completed.
        - 'priority': The priority level of the task.
    Process:
        - Creates a new task as a list with the provided description, completion status, and priority.
        - Appends the newly created task to the 'tasks' list.
    Output:
        - Prints a confirmation message indicating that the task with the given description and priority has been added.
    """

def add_task(tasks, task_description, completed, priority):
    task = [task_description, completed, priority]
    tasks.append(task)
    print(f"Task '{task_description}' with priority '{priority}' added.")

# Function to mark a task as completed

    """
    Input:
        - 'tasks': A list containing tasks.
        - 'task_index': The index of the task to mark as completed.
    Process:
        - Checks if the provided task index is within the valid range.
        - If the task index is valid, it marks the corresponding task as completed by setting its completion status to True.
    Output:
        - Prints a confirmation message indicating that the specified task has been marked as completed.
        - If the task index is not valid, it prints an error message indicating an invalid task index.
    """

def mark_task_as_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1][1] = True
        print(f"Task '{tasks[task_index - 1][0]}' marked as completed.")
    else:
        print("Invalid task index.")

# Function to load data from a file

"""
    Input:
        - 'notes': A list to store notes.
        - 'tasks': A list to store tasks.
    Process:
        - Attempts to open and read data from a file named 'notes_and_tasks.txt'.
        - Reads each line from the file and processes it to populate 'notes' and 'tasks' lists.
        - Data in the file is organized into 'Notes' and 'Tasks' sections.
        - For 'Notes' section, lines are expected to be in the format "Category: Content".
        - For 'Tasks' section, lines are expected to be in the format "[X] Description (Priority: PriorityLevel)".
        - If the file is not found, it prints a message indicating that the file is not found and starts with empty data.
    Output:
        - Loads data from the file into the 'notes' and 'tasks' lists.
        - If the file is not found, it prints an error message and starts with empty data.
    """

def load_from_file(notes, tasks):
    try:
        with open("notes_and_tasks.txt", "r") as file:
            data = file.readlines()
            category = None
            for line in data:
                line = line.strip()
                if line == "Notes:":
                    category = "Notes"
                elif line == "Tasks:":
                    category = "Tasks"
                elif line and category:
                    if category == "Notes":
                        # Split the line into category and content
                        parts = line.split(": ", 1)
                        if len(parts) == 2:
                            notes.append((parts[0], parts[1]))
                    elif category == "Tasks":
                        # Split the line into description, completion status, and priority
                        parts = line.split(" (Priority: ", 1)
                        description = parts[0]
                        if len(parts) == 2:
                            priority = parts[1][:-1]  # Remove the closing parenthesis
                        else:
                            priority = "No Priority"
                        completed = "X" in description
                        tasks.append([description, completed, priority])
    except FileNotFoundError:
        print("File 'notes_and_tasks.txt' not found. Starting with empty data.")

# Function to save notes and tasks to a file

    """
    Input:
        - 'notes': A list containing notes.
        - 'tasks': A list containing tasks.
    Process:
        - Opens a file named 'notes_and_tasks.txt' for writing.
        - Writes the 'Notes' section and the content of each note to the file.
        - Writes the 'Tasks' section and the content of each task to the file, including completion status and priority.
    Output:
        - Saves the notes and tasks to a file in a specific format.
    """

def save_to_file(notes, tasks):
    with open("notes_and_tasks.txt", "w") as file:
        file.write("Notes:\n")
        for note in notes:
            file.write(f"{note[0]}: {note[1]}\n")
        file.write("\nTasks:\n")
        for task in tasks:
            completed = "X" if task[1] else " "
            file.write(f"[{completed}] {task[0]} (Priority: {task[2]})\n")

# Function to remove a note by criteria

    """
    Input:
        - 'notes': A list containing stored notes.
    Process:
        - Checks if there are notes in the 'notes' list.
        - If there are no notes, it prints a message indicating that no notes have been recorded.
        - If there are notes, it prompts the user to enter criteria (e.g., content, category) to identify the note to remove.
        - The function then identifies notes that match the specified criteria and displays them.
        - It allows the user to select a matching note to remove by index.
    Output:
        - Removes the selected note based on the user's choice.
        - Prints confirmation messages, including details of the removed note.
        - If no matching notes are found, it prints a message indicating that no notes matching the criteria were found.
    """

def remove_note_by_criteria(notes):
    if not notes:
        print("No notes recorded.")
        return
    
    criteria = input("Enter criteria to identify the note (e.g., content, category): ").strip().lower()
    search_term = input(f"Enter the {criteria} of the note to remove: ").strip()
    
    matching_notes = []
    
    for i, note in enumerate(notes, 1):
        if search_term.lower() in note[0].lower() or search_term.lower() in note[1].lower():
            matching_notes.append((i, note))
    
    if not matching_notes:
        print(f"No notes matching the {criteria} '{search_term}' found.")
    else:
        print("Matching notes:")
        for index, note in matching_notes:
            print(f"{index}. Category: {note[0]}, Content: {note[1]}")
        
        note_index = int(input("Enter the index of the note to remove: "))
        
        if 1 <= note_index <= len(matching_notes):
            index_to_remove, _ = matching_notes[note_index - 1]
            removed_note = notes.pop(index_to_remove - 1)
            print(f"Note '{removed_note[1]}' in category '{removed_note[0]}' removed.")
        else:
            print("Invalid note index.")

# Function to edit a note
    """
    Input:
        - 'notes': A list containing stored notes.
        - 'note_index': The index of the note to edit.
    Process:
        - Checks if the provided note index is within the valid range.
        - If the note index is valid, it allows the user to enter a new category and content for the note.
        - If the user provides new category or content, it updates the note with the new values.
        - If the user does not provide new category or content, it keeps the existing values.
    Output:
        - Prints a confirmation message indicating that the note has been edited with the new category and content.
        - If the note index is not valid, it prints an error message indicating an invalid note index.
    """

def edit_note(notes, note_index):
    if 1 <= note_index <= len(notes):
        note = notes[note_index - 1]
        new_category = input(f"Enter the new category (or press Enter to keep the current category): ")
        new_content = input(f"Enter the new content (or press Enter to keep the current content): ")

        if new_category:
            category = new_category
        else:
            category = note[0]

        if new_content:
            content = new_content
        else:
            content = note[1]

        notes[note_index - 1] = (category, content)
        print(f"Note edited in category '{category}' with new content '{content}'")
    else:
        print("Invalid note index.")

# Function to sort tasks by priority

"""
    Input:
        - 'tasks': A list containing tasks.
    Process:
        - Sorts the tasks based on the priority column (index 2) in ascending order.
        - Prints the sorted tasks along with their priority and completion status.
    Output:
        - Prints a message indicating that the tasks have been sorted by priority.
    """

def sort_tasks_by_priority(tasks):
    # Sort tasks by the priority column (index 2) in ascending order
    tasks.sort(key=lambda task: task[2])
    print("Tasks sorted by priority:")
    for i, task in enumerate(tasks, 1):
        completed = "X" if task[1] else " "
        print(f"{i}. Priority: {task[2]}, Description: {task[0]} [{completed}]")

# Function to remove all data (notes and tasks)

    """
    Input:
        - 'notes': A list containing stored notes.
        - 'tasks': A list containing tasks.
    Process:
        - Prompts the user to confirm the deletion of all notes and tasks.
        - If the user confirms with "yes," it clears both 'notes' and 'tasks' lists, effectively deleting all data.
    Output:
        - Prints a confirmation message when all notes and tasks have been deleted.
        - If the user cancels the deletion, it prints a message indicating that the deletion has been canceled.
    """

def remove_all_data(notes, tasks):
    confirm = input("Are you sure you want to delete all notes and tasks? (yes/no): ")
    if confirm.lower() == "yes":
        notes.clear()
        tasks.clear()
        print("All notes and tasks have been deleted.")
    else:
        print("Deletion canceled.")

# Function to import data from a text file

"""
    Input:
        - 'notes': A list containing notes.
        - 'tasks': A list containing tasks.
    Process:
        - Prompts the user to enter the name of the file from which to import data.
        - Attempts to open and read data from the specified file.
        - Reads each line from the file and processes it to populate 'notes' and 'tasks' lists.
        - Data in the file is organized into 'Notes' and 'Tasks' sections.
        - For 'Notes' section, lines are expected to be in the format "Category: Content".
        - For 'Tasks' section, lines are expected to be in the format "[X] Description (Priority: PriorityLevel) (Due Date: Date)".
        - If the file is not found, it prints a message indicating that the file is not found, and no data is imported.
    Output:
        - Loads data from the specified file into the 'notes' and 'tasks' lists.
        - Prints a message indicating that data has been successfully imported from the file.
        - If the file is not found, it prints an error message indicating that the file was not found, and no data is imported.
    """

def import_data_from_file(notes, tasks):
    filename = input("Enter the name of the file to import data from: ")
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            category = None
            for line in data:
                line = line.strip()
                if line == "Notes:":
                    category = "Notes"
                elif line == "Tasks:":
                    category = "Tasks"
                elif line and category:
                    if category == "Notes":
                        # Split the line into category and content
                        parts = line.split(": ", 1)
                        if len(parts) == 2:
                            notes.append((parts[0], parts[1]))
                    elif category == "Tasks":
                        # Split the line into description, completion status, priority, and due date
                        parts = line.split(" (Priority: ", 1)
                        description = parts[0]
                        if len(parts) == 2:
                            priority, due_date = parts[1].split(") (Due Date: ", 1)
                            completed = "X" in description
                            tasks.append([description, completed, priority, due_date[:-1]])
                        else:
                            completed = "X" in description
                            priority = "No Priority"
                            due_date = None
                            tasks.append([description, completed, priority, due_date])
        print(f"Data imported from '{filename}' successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No data imported.")

# Main function of the notes and tasks manager

"""
Input:
        - No direct input parameters.
    Process:
        - Initializes two lists, 'notes' and 'tasks', to store notes and tasks.
        - Loads data from a file into 'notes' and 'tasks' using the 'load_from_file' function.
        - Displays a menu with various options for managing notes and tasks.
        - Processes the user's choice, including options to create notes, display notes, add tasks, mark tasks as completed,
          save data to a file, remove notes, edit notes, sort tasks by priority, remove all data, and import data from a text file.
    Output:
        - Provides a user interface for managing notes and tasks, allowing the user to perform various actions.
        - Executes the selected actions and provides feedback to the user.
    """

def main():
    notes = []  # Use a list to store notes
    tasks = []  # Use a list to store tasks

    load_from_file(notes, tasks)

    while True:
        print("\nMenu:")
        print("1. Create a new note")
        print("2. Display notes")
        print("3. Add a task")
        print("4. Mark a task as completed")
        print("5. Save to a file")
        print("6. Remove a note")
        print("7. Edit a note")
        print("8. Sort tasks by priority")
        print("9. Remove all data (notes and tasks)")
        print("10. Import data from a text file")
        print("11. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter the note's category: ")
            content = input("Enter the note's content: ")
            create_note(notes, category, content)
        elif choice == "2":
            display_notes(notes)
        elif choice == "3":
            task_description = input("Enter the task description: ")
            completed = False
            priority = input("Enter the task priority (e.g., Low, Medium, High): ")
            add_task(tasks, task_description, completed, priority)
        elif choice == "4":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            mark_task_as_completed(tasks, task_index)
        elif choice == "5":
            save_to_file(notes, tasks)
            print("Data saved to 'notes_and_tasks.txt'.")
        elif choice == "6":
            remove_note_by_criteria(notes)
        elif choice == "7":
            note_index = int(input("Enter the index of the note to edit: "))
            edit_note(notes, note_index)
        elif choice == "8":
            sort_tasks_by_priority(tasks)
        elif choice == "9":
            remove_all_data(notes, tasks)
        elif choice == "10":
            import_data_from_file(notes, tasks)
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")


# Start the program by calling the main function
main()