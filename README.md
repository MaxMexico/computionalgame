# Note and Task Manager

I have completely changed my plans! After some consideration, I found that the idea of a game wasn't very useful. Instead, I realized the need for a task and note manager to help me organize my days as a student.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [How to use it](#how-to-use-it)
- [How the user execute it](#how-does-the-user-execute-it)
- [Technical dependencies](#technical-dependencies)
- [Test Plan](#Test-plan)



## Introduction

This project is a personal note and task manager designed to assist students in organizing their daily tasks and notes efficiently. It offers a simple yet powerful way to keep track of your assignments, lectures, and more.

## Features

- Create and manage notes with categories.
- Add, complete, and prioritize tasks.
- Load and save data to a file.
- Remove notes and tasks by criteria.
- Edit notes.
- Sort tasks by priority.

## How to use it

The note and task manager is very intuitive, follow the terminal's indications according to the menu or the various requests

## How does the user execute it

Download the repositery from Github

-Change your current directory to the project folder: cd computionalgame
-Execute the main Python script to start the Note and Task Manager: python main.py
-Follow the on-screen menu options to interact with the manager and manage your notes and tasks

## Technical dependencies

You do not need a special library for run this program only a python interpreter and a terminal. So you can use the program without worrying about installing any additional libraries or modules.

## Test plan
You can find all the test cases for all the functions in the program here.

#### Function create_note :
Menu:
1. Create a new note
2. Display notes
3. Add a task
4. Mark a task as completed
5. Save to a file
6. Remove a note
7. Edit a note
8. Sort tasks by priority
9. Remove all data (notes and tasks)
10. Quit
Choose an option: 1
Enter the note's category: School
Enter the note's content: Do the homeworks
Note added in the 'School' category.

#### Function display_notes :
Choose an option: 2
Available categories:
- School
- sport
Enter the category name to display notes: sport
Notes in the 'sport' category:
- do sport

#### Function add_task:
Choose an option: 3
Enter the task description: Clean the house
Enter the task priority (e.g., Low, Medium, High): High
Task 'Clean the house' with priority 'High' added.

#### Function mark_task_as_completed:
Choose an option: 4
Enter the index of the task to mark as completed: 1
Task 'Clean the house' marked as completed.

#### Function save_to_file:
Choose an option: 5
Data saved to 'notes_and_tasks.txt'.

#### Function remove_note_by_criteria:
Choose an option: 6
Enter criteria to identify the note (e.g., content, category): sport
Enter the sport of the note to remove:
Matching notes:
1. Category: sport, Content: do sport
2. Category: shopping, Content: go to the grocery store
Enter the index of the note to remove: 1
Note 'do sport' in category 'sport' removed.

##### Function edit_note:
Choose an option: 7
Enter the index of the note to edit: 1
Enter the new category (or press Enter to keep the current category):
Enter the new content (or press Enter to keep the current content): Go to the grocery store "today" 
Note edited in category 'shopping' with new content 'Go to the grocery store "today"'

#### Function sort_tasks_by_priority:
Choose an option: 8
Tasks sorted by priority:
1. Priority: High, Description: clean the house [ ]
2. Priority: Medium, Description: Mail the teacher  [ ]

#### Function remove_all_data:
Choose an option: 9
Are you sure you want to delete all notes and tasks? (yes/no): yes
All notes and tasks have been deleted.

#### Function import_data_from_file:
Choose an option: 10
Enter the name of the file to import data from: Note_Test
Data imported from 'Note_Test' successfully.

### Hope this manager will help as much as it helps me everyday 
### Have fun !
## 🇲🇽 ¡Viva México! 🇲🇽

![Mexican flag](https://github.com/MaxMexico/computionalgame/blob/08a504434ee7207e30b4fa1016b011464e39d99a/t%C3%A9l%C3%A9chargement.png)
By MaxMexico 
2023
