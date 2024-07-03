# import tkinter as tk
# from tkinter import ttk

# class Task:
#     def __init__(self, text, priority):
#         self.text = text
#         self.priority = priority
#         self.completed = False

# class ToDoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List App")
#         self.root.geometry("400x600")
#         self.root.configure(bg="#f0f0f0")

#         self.tasks = []

#         self.create_widgets()

#     def create_widgets(self):
#         # Header
#         header_label = tk.Label(self.root, text="To-Do List", font=('Helvetica', 24, 'bold'), bg="#4CAF50", fg="white", padx=10, pady=5)
#         header_label.pack(fill=tk.X)

#         # Entry and Buttons
#         entry_frame = tk.Frame(self.root, bg="#f0f0f0")
#         entry_frame.pack(pady=20, padx=10)

#         self.task_entry = tk.Entry(entry_frame, font=('Arial', 14), bg="#ffffff", bd=2, relief=tk.FLAT, width=24)
#         self.task_entry.grid(row=0, column=0, padx=10, ipady=8, sticky="ew")

#         add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task, style="TButton")
#         add_button.grid(row=0, column=1, padx=10, ipady=8)

#         # Task List
#         list_frame = tk.Frame(self.root, bg="#f0f0f0")
#         list_frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

#         self.task_text = tk.Text(list_frame, wrap=tk.WORD, height=12, width=24, bd=0, font=('Arial', 12), spacing1=5, spacing2=2, spacing3=5)
#         self.task_text.pack(fill=tk.BOTH, expand=True)
#         self.task_text.tag_configure("completed", overstrike=True)

#         # Action Buttons
#         buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
#         buttons_frame.pack(pady=10)

#         update_button = ttk.Button(buttons_frame, text="Toggle Completion", command=self.toggle_completion, style="TButton")
#         update_button.grid(row=0, column=0, padx=5, ipady=8)

#         delete_button = ttk.Button(buttons_frame, text="Delete Task", command=self.delete_task, style="TButton")
#         delete_button.grid(row=0, column=1, padx=5, ipady=8)

#         # Priority Combobox
#         priority_frame = tk.Frame(self.root, bg="#f0f0f0")
#         priority_frame.pack(pady=10)

#         priority_label = tk.Label(priority_frame, text="Priority:", font=('Arial', 14), bg="#f0f0f0")
#         priority_label.grid(row=0, column=0, padx=5)

#         self.priority_var = tk.StringVar()
#         self.priority_var.set("Low")

#         priority_menu = ttk.Combobox(priority_frame, textvariable=self.priority_var, values=["Low", "Medium", "High"],
#                                      style="TCombobox")
#         priority_menu.grid(row=0, column=1, padx=5)

#         # Set the style for buttons and combobox
#         style = ttk.Style()
#         style.configure("TButton", background="#4CAF50", font=('Arial', 12), width=15)
#         style.map("TButton", background=[('active', '#45a049')])

#         style.configure("TCombobox", font=('Arial', 12), width=10)

#     def add_task(self):
#         task_text = self.task_entry.get()
#         priority = self.priority_var.get()
#         if task_text:
#             task = Task(text=task_text, priority=priority)
#             self.tasks.append(task)
#             self.update_task_list()

#     def toggle_completion(self):
#         selected_index = self.task_text.index(tk.SEL_FIRST)
#         if selected_index:
#             task_index = int(selected_index.split('.')[0]) - 1
#             task = self.tasks[task_index]
#             task.completed = not task.completed
#             self.update_task_list()

#     def delete_task(self):
#         selected_index = self.task_text.index(tk.SEL_FIRST)
#         if selected_index:
#             task_index = int(selected_index.split('.')[0]) - 1
#             del self.tasks[task_index]
#             self.update_task_list()

#     def update_task_list(self):
#         self.task_text.delete(1.0, tk.END)
#         for index, task in enumerate(self.tasks, start=1):
#             task_text = f"{index}. [{task.priority}] {task.text}\n"
#             if task.completed:
#                 self.task_text.insert(tk.END, task_text, "completed")
#             else:
#                 self.task_text.insert(tk.END, task_text)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = ToDoApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, text, priority):
        self.text = text
        self.priority = priority
        self.completed = False

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_label = tk.Label(self.root, text="To-Do List", font=('Helvetica', 24, 'bold'), bg="#4CAF50", fg="white", padx=10, pady=5)
        header_label.pack(fill=tk.X)

        # Entry and Buttons
        entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        entry_frame.pack(pady=20, padx=10)

        self.task_entry = tk.Entry(entry_frame, font=('Arial', 14), bg="#ffffff", bd=2, relief=tk.FLAT, width=24)
        self.task_entry.grid(row=0, column=0, padx=10, ipady=8, sticky="ew")

        add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task, style="TButton")
        add_button.grid(row=0, column=1, padx=10, ipady=8)

        # Task List
        list_frame = tk.Frame(self.root, bg="#f0f0f0")
        list_frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

        self.task_text = tk.Text(list_frame, wrap=tk.WORD, height=12, width=24, bd=0, font=('Arial', 12), spacing1=5, spacing2=2, spacing3=5)
        self.task_text.pack(fill=tk.BOTH, expand=True)
        self.task_text.tag_configure("completed", overstrike=True)

        # Action Buttons
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(pady=10)

        update_button = ttk.Button(buttons_frame, text="Toggle Completion", command=self.toggle_completion, style="TButton")
        update_button.grid(row=0, column=0, padx=5, ipady=8)

        delete_button = ttk.Button(buttons_frame, text="Delete Task", command=self.delete_task, style="TButton")
        delete_button.grid(row=0, column=1, padx=5, ipady=8)

        # Priority Combobox
        priority_frame = tk.Frame(self.root, bg="#f0f0f0")
        priority_frame.pack(pady=10)

        priority_label = tk.Label(priority_frame, text="Priority:", font=('Arial', 14), bg="#f0f0f0")
        priority_label.grid(row=0, column=0, padx=5)

        self.priority_var = tk.StringVar()
        self.priority_var.set("Low")

        priority_menu = ttk.Combobox(priority_frame, textvariable=self.priority_var, values=["Low", "Medium", "High"],
                                     style="TCombobox")
        priority_menu.grid(row=0, column=1, padx=5)

        # Set the style for buttons and combobox
        style = ttk.Style()
        style.configure("TButton", font=('Arial', 12), width=15)

        style.configure("TCombobox", font=('Arial', 12), width=10)

    def add_task(self):
        task_text = self.task_entry.get()
        priority = self.priority_var.get()
        if task_text:
            task = Task(text=task_text, priority=priority)
            self.tasks.append(task)
            self.update_task_list()
            # Clear the entry after adding task
            self.task_entry.delete(0, tk.END)

    def toggle_completion(self):
        selected_index = self.task_text.index(tk.SEL_FIRST)
        if selected_index:
            task_index = int(selected_index.split('.')[0]) - 1
            task = self.tasks[task_index]
            task.completed = not task.completed
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_text.index(tk.SEL_FIRST)
        if selected_index:
            task_index = int(selected_index.split('.')[0]) - 1
            del self.tasks[task_index]
            self.update_task_list()

    def update_task_list(self):
        self.task_text.delete(1.0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            task_text = f"{index}. {task.text}\n"
            tag_name = f"priority_{task.priority.lower()}"
            if task.completed:
                tag_name += "_completed"
            self.task_text.insert(tk.END, task_text, tag_name)

            # Configure tag color
            self.task_text.tag_configure(tag_name, foreground=self.get_priority_color(task.priority))

    def get_priority_color(self, priority):
        priority_color = {"Low": "green", "Medium": "black", "High": "red"}
        return priority_color.get(priority, "black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
