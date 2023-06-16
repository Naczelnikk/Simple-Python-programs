import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox_uncompleted.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        if listbox_uncompleted.curselection():
            index = listbox_uncompleted.curselection()[0]
            listbox_uncompleted.delete(index)
        elif listbox_completed.curselection():
            index = listbox_completed.curselection()[0]
            listbox_completed.delete(index)
    except IndexError:
        pass

def complete_task():
    try:
        index = listbox_uncompleted.curselection()[0]
        task = listbox_uncompleted.get(index)
        listbox_uncompleted.delete(index)
        listbox_completed.insert(tk.END, task)
    except IndexError:
        pass

def main():
    global entry, listbox_uncompleted, listbox_completed

    root = tk.Tk()
    root.title("To-Do App")

    label_uncompleted = tk.Label(root, text="Uncompleted Tasks", font=("Helvetica", 14, "bold"))
    label_uncompleted.pack(pady=5, padx=10, anchor=tk.W)

    listbox_uncompleted = tk.Listbox(root, font=("Helvetica", 16), bd=0, fg="black")
    listbox_uncompleted.pack(pady=5, padx=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

    label_completed = tk.Label(root, text="Completed Tasks", font=("Helvetica", 14, "bold"))
    label_completed.pack(pady=5, padx=10, anchor=tk.W)

    listbox_completed = tk.Listbox(root, font=("Helvetica", 16), bd=0, fg="gray")
    listbox_completed.pack(pady=5, padx=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, font=("Helvetica", 16), fg="gray")
    entry.insert(tk.END, "Type task here")
    entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END))
    entry.bind("<FocusOut>", lambda event: entry.insert(tk.END, "Type task here") if entry.get() == "" else None)
    entry.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=10)

    add_button = tk.Button(frame, text="Add Task", command=add_task)
    add_button.grid(row=0, column=0)

    delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
    delete_button.grid(row=0, column=1)

    complete_button = tk.Button(frame, text="Complete Task", command=complete_task)
    complete_button.grid(row=0, column=2)

    root.mainloop()

if __name__ == "__main__":
    main()
