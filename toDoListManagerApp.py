import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append({'text': task, 'done': False})
            messagebox.showinfo('Task Added', f'Task "{task}" added successfully!')

    def get_tasks(self):
        return self.tasks

    def mark_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks[index]['text']
            del self.tasks[index]
            messagebox.showinfo('Task Deleted', f'Task "{deleted_task}" deleted successfully!')

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('600x600')
        self.root.minsize(600, 600)
        self.root.maxsize(600, 600)
        self.root.configure(bg='pink')

        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(root, width=50, font=('Comic Sans MS', 14))
        self.task_entry.pack(padx=50, pady=20)

        self.add_button = tk.Button(root, text='Add Task', command=self.add_task, font=('Comic Sans MS', 14),
                                     bg='light blue', bd=5, padx=10, pady=5)
        self.add_button.pack(pady=10)

        self.tasks_display = tk.Listbox(root, height=10, width=50, font=('Comic Sans MS', 12), bg='light blue')
        self.tasks_display.pack(padx=50, pady=20)
        self.tasks_display.bind('<ButtonRelease-1>', self.highlight_task)

        self.mark_done_button = tk.Button(root, text='Mark Task as Done', command=self.mark_as_done,
                                          font=('Comic Sans MS', 14), bg='light blue', bd=5, padx=10, pady=5)
        self.mark_done_button.pack(pady=10)

        self.delete_button = tk.Button(root, text='Delete Task', command=self.delete_task, font=('Comic Sans MS', 14),
                                       bg='red', bd=5, padx=10, pady=5)
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_display()
            self.task_entry.delete(0, tk.END)

    def update_display(self):
        tasks = self.todo_list.get_tasks()
        self.tasks_display.delete(0, tk.END)
        for task in tasks:
            status = "[ ]" if not task['done'] else "[x]"
            self.tasks_display.insert(tk.END, f'{status} {task["text"]}')

    def highlight_task(self, event):
        selected_index = self.tasks_display.nearest(event.y)
        self.tasks_display.selection_clear(0, tk.END)
        self.tasks_display.selection_set(selected_index)

    def mark_as_done(self):
        selected_index = self.tasks_display.curselection()
        if selected_index:
            self.todo_list.mark_as_done(selected_index[0])
            self.update_display()

    def delete_task(self):
        selected_index = self.tasks_display.curselection()
        if selected_index:
            self.todo_list.delete_task(selected_index[0])
            self.update_display()

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
