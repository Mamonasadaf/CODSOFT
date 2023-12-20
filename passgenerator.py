import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar, messagebox

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Password Generator')
        self.master.geometry('300x300')
        self.master.configure(bg='light gray')

        self.create_widgets()

    def create_widgets(self):
        # Label and Entry for user input
        label_instruction = Label(self.master, text='Password Generator\nEnter desired length:', bg='light gray')
        label_instruction.grid(row=0, column=0, columnspan=2, pady=5)

        self.length_entry = Entry(self.master, width=10, font=('Arial', 12))
        self.length_entry.grid(row=1, column=0, columnspan=2, pady=5)

        # Button to generate password
        generate_button = Button(self.master, text='Generate Password', command=self.generate_password, bg='steel blue', fg='white')
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Label and Text for displaying generated password
        label_result = Label(self.master, text='Your generated password:', bg='light gray')
        label_result.grid(row=3, column=0, columnspan=2, pady=5)

        self.result_text = Text(self.master, height=1, width=30, font=('Arial', 12), bd=2, relief=tk.SUNKEN, wrap=tk.WORD)
        self.result_text.grid(row=4, column=0, columnspan=2, pady=5)

        # Scrollbar for the result_text
        scrollbar = Scrollbar(self.master, command=self.result_text.yview)
        scrollbar.grid(row=4, column=2, sticky='ns')
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Button to clear password
        clear_button = Button(self.master, text='Clear Password', command=self.clear_password, bg='lightcoral', fg='white')
        clear_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Message at the bottom
        message_label = Label(self.master, text='Hopefully you liked it!', bg='light gray')
        message_label.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid number for the length.')
            return

        password = self.generate_password_helper(length)
        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, password)

    def generate_password_helper(self, length):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        all_characters = lower_case + upper_case + digits + special_characters
        length = max(length, 8)

        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password

    def clear_password(self):
        self.result_text.delete('1.0', tk.END)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
