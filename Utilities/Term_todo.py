"""
Challange: Terminal based task manager 

Create a Python Scipt that lets the user manage a to-do list
directly from the terminal

Your program should:- 
1. Ask the user to 
    - add a task
    - View all tasks
    - Mark a task as complete
    - Delete a Task 
    - Exit the app 

2. Save all the tasks in a text file named 'tasks.txt' so that the data
persists between runs.

3. Display tasks with an index number and " if task("done") else " " "
    print(f"{i}. {[checkbox]} {task{'text'} ")
"""
START = f"-------- TASK LIST MANAGER --------"
MENU = [
    "1 - ADD TASKS", 
    "2 - VIEW TASKS",
    "3 - MARK TASKS AS COMPLETE",
    "4 - DELETE TASKS",
    "Q - EXIT"
]

def selection():
    choice = input("\nINPUT: ").strip()
    return choice

def add_tasks(tasks):
    task = input("ENTER THE TASK: ").strip()
    tasks.append(task)

def render_incomplete_tasks(tasks):
    pass

def render_complete_tasks(tasks):
    pass

def delete_complete_tasks(tasks):
    pass

def main():
    tasks = []
    while True:
        print(START)
        for item in MENU:
            print(f"\n{item}")
        choice = selection()
        match choice:
            case "1":
                add_tasks(tasks)
            case "2":
                render_incomplete_tasks(tasks)
            case "3":
                render_complete_tasks(tasks)
            case "4":
                render_complete_tasks(tasks)
                delete_complete_tasks(tasks)
            case "q" | "Q":
                return
            case _:
                continue

if __name__ == "__main__":
    main()
