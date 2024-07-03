import tkinter as tk
from tkinter import font

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")

        # Custom color scheme
        bg_color = "#282C35"
        button_bg_color = "#3E4049"
        button_fg_color = "white"
        display_fg_color = "white"

        # Entry widget to display the current expression
        self.expression_var = tk.StringVar()
        entry_font = font.Font(family='Arial', size=14)
        self.entry = tk.Entry(root, textvariable=self.expression_var, font=entry_font, bd=10,
                              insertwidth=4, width=14, justify='right', fg=display_fg_color, bg=bg_color)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout for the calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place the buttons
        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 12),
                      command=lambda text=button_text: self.button_click(text),
                      fg=button_fg_color, bg=button_bg_color).grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Add Backspace, Clear, and Memory buttons
        tk.Button(root, text="⌫", padx=20, pady=20, font=('Arial', 12),
                  command=self.backspace, fg=button_fg_color, bg=button_bg_color).grid(row=5, column=0, sticky="nsew")
        tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 12),
                  command=self.clear, fg=button_fg_color, bg=button_bg_color).grid(row=5, column=1, sticky="nsew")
        tk.Button(root, text="M+", padx=20, pady=20, font=('Arial', 12),
                  command=self.memory_add, fg=button_fg_color, bg=button_bg_color).grid(row=5, column=2, sticky="nsew")
        tk.Button(root, text="MR", padx=20, pady=20, font=('Arial', 12),
                  command=self.memory_recall, fg=button_fg_color, bg=button_bg_color).grid(row=5, column=3, sticky="nsew")

        # Configure grid weights to make the calculator expandable
        for i in range(6):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i, weight=1)

        # Memory variable
        self.memory = 0

    def button_click(self, text):
        current_expression = self.expression_var.get()

        if text == '=':
            try:
                result = str(eval(current_expression))
                self.expression_var.set(result)
            except Exception as e:
                self.expression_var.set("Error")
        else:
            new_expression = current_expression + text
            self.expression_var.set(new_expression)

    def backspace(self):
        current_expression = self.expression_var.get()
        new_expression = current_expression[:-1]
        self.expression_var.set(new_expression)

    def clear(self):
        self.expression_var.set("")

    def memory_add(self):
        current_result = self.expression_var.get()
        try:
            current_result = str(eval(current_result))
            self.memory += float(current_result)
        except Exception as e:
            self.expression_var.set("Error")

    def memory_recall(self):
        self.expression_var.set(str(self.memory))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
