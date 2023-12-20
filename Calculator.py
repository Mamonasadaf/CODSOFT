import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.master.geometry('400x600')
        self.master.configure(bg='light pink')

        self.result_var = tk.StringVar()
        self.result_var.set('0')

        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying the result
        result_entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 24), bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
        result_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', 'x',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.master, text=button, font=('Arial', 16), bg='steel blue', padx=10, pady=10, bd=2,
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights to make buttons expandable
        for i in range(1, 5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        elif button == 'C':
            self.result_var.set('0')
        else:
            if current_text == '0':
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
