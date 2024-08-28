import tkinter as tk

def add_task(event=None):
    task = task_entry.get()
    if task:
        tasks.insert(0, task)
        task_entry.delete(0, tk.END)
        update_listbox()

def delete_task():
    selected_task_index = task_listBox.curselection()
    if selected_task_index:
        task = task_listBox.get(selected_task_index)
        if task.endswith(" (Выполнено)"):
            completed_tasks.remove(task)
        else:
            tasks.remove(task)
        update_listbox()

def mark_task():
    selected_task_index = task_listBox.curselection()
    if selected_task_index:
        task = task_listBox.get(selected_task_index)
        if "(Выполнено)" not in task:
            tasks.remove(task)
            completed_task = task + " (Выполнено)"
            completed_tasks.append(completed_task)
            update_listbox()

def update_listbox():
    task_listBox.delete(0, tk.END)
    for task in tasks:
        task_listBox.insert(tk.END, task)
    for task in completed_tasks:
        task_listBox.insert(tk.END, task)

def validate_input(new_value):
    return len(new_value) <= 30

root = tk.Tk()
root.title("Список дел")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 400

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

validate_command = root.register(validate_input)

task_entry = tk.Entry(root, width=30, validate="key", validatecommand=(validate_command, '%P'))
task_entry.pack(pady=10)
task_entry.bind('<Return>', add_task)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task, width=20)
add_task_button.pack(pady=10)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, width=20)
delete_button.pack(pady=10)

mark_button = tk.Button(root, text="Отметить задачу как выполненную", command=mark_task, width=25)
mark_button.pack(pady=10)

task_listBox = tk.Listbox(root, height=10, width=50)
task_listBox.pack(pady=10, padx=10)

tasks = []
completed_tasks = []

root.mainloop()
