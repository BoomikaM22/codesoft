import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    try:
        task_index = int(listbox.curselection()[0])
        tasks.delete(task_index)
    except IndexError:
        pass

app = tk.Tk()
app.title("To-Do List App")
frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, height=10, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(app, width=50)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", width=48, command=add_task)
add_button.pack()

remove_button = tk.Button(app, text="Remove Task", width=48, command=remove_task)
remove_button.pack()
tasks = listbox
app.mainloop()
