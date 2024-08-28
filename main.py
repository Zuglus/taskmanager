import tkinter as tk

root = tk.Tk()

root.title("Список дел")
root.configure(bg="lavender")

task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу")
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу")
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить задачу как выполненную")
mark_button.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width = 50, bg="DeepPink1")
task_listBox.pack(pady=10)

root.mainloop()