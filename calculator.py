import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Numeric buttons on one side
        numbers = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0)
        ]

        # Calculation buttons on the other side
        calculations = [
            ('/', 1, 3), ('*', 2, 3), ('-', 3, 3),
            ('+', 4, 3), ('=', 4, 2), ('C', 5, 0),
            ('sqrt', 5, 1), ('^', 5, 2), ('%', 5, 3)
        ]

        # Create numeric buttons
        for (text, row, column) in numbers:
            self.create_button(text, row, column, "#FFCCCB")

        # Create larger "0" button that spans two columns
        zero_button = tk.Button(self, text='0', padx=20, pady=60, font=("Arial", 18),
                                command=lambda: self.on_button_click('0'), bg="#FFCCCB", fg="#000",
                                activebackground="#FFAAAA")
        zero_button.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

        # Create calculation buttons
        for (text, row, column) in calculations:
            self.create_button(text, row, column, "#FFABAB")

    def create_button(self, text, row, column, color):
        button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda: self.on_button_click(text), bg=color, fg="#000",
                           activebackground="#FFAAAA")
        button.grid(row=row, column=column, sticky='nsew', padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            self.calculate_result()
        elif char == 'sqrt':
            try:
                value = float(self.display.get())
                result = math.sqrt(value)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                messagebox.showerror("Error", "Invalid input")
        elif char == '^':
            self.display.insert(tk.END, '**')
        elif char == '%':
            self.calculate_percentage()
        else:
            self.display.insert(tk.END, char)

    def calculate_result(self):
        try:
            expression = self.display.get().replace('^', '**')
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    def calculate_percentage(self):
        try:
            value = float(self.display.get())
            result = value / 100
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
