import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold")).pack(pady=10)

        # Entry for new task
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(padx=20, pady=10, fill=tk.X)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", width=12, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Task", width=12, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Clear All", width=12, command=self.clear_tasks).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Save Tasks", width=12, command=self.save_tasks).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Load Tasks", width=26, command=self.load_tasks).grid(row=2, column=0, columnspan=2, pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), height=15, selectbackground="lightblue")
        self.task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
        else:
            messagebox.showwarning("Delete Error", "Please select a task to delete.")

    def clear_tasks(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            self.task_listbox.delete(0, tk.END)

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully.")

    def load_tasks(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            self.task_listbox.delete(0, tk.END)
            with open(file, "r") as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

