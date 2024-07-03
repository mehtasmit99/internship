import tkinter as tk
from tkinter import ttk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables for checkbox states
        self.include_alpha = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        # Styling
        style = ttk.Style()

        # Background color
        style.configure("TFrame", background="#F8B195")
        style.configure("TLabel", foreground="#F67280", font=('Quicksand', 12))
        style.configure("TCheckbutton", font=('Quicksand', 12), background="#C06C84", foreground="#fff")
        style.configure("TButton", font=('Quicksand', 12), background="#6C5B7B")
        style.configure("TEntry", font=('Quicksand', 12), fieldbackground="#355C7D")

        # Frame
        frame = ttk.Frame(root, padding=(20, 20, 20, 20), style="TFrame")
        frame.grid(row=0, column=0, sticky="nsew")

        # Entry for specifying password length
        self.length_label = ttk.Label(frame, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.length_entry = ttk.Entry(frame)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Checkboxes for character types
        self.alpha_checkbox = ttk.Checkbutton(frame, text="Include Alphabetic", variable=self.include_alpha, style="TCheckbutton")
        self.alpha_checkbox.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

        self.num_checkbox = ttk.Checkbutton(frame, text="Include Numbers", variable=self.include_numbers, style="TCheckbutton")
        self.num_checkbox.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

        self.special_checkbox = ttk.Checkbutton(frame, text="Include Special Characters", variable=self.include_special, style="TCheckbutton")
        self.special_checkbox.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

        # Button to generate password
        self.generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password, style="TButton")
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Display area for generated password
        self.result_label = ttk.Label(frame, text="Your Password:")
        self.result_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.result_entry = ttk.Entry(frame, state="readonly", style="TEntry")
        self.result_entry.grid(row=5, column=1, padx=10, pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        include_alpha = self.include_alpha.get()
        include_numbers = self.include_numbers.get()
        include_special = self.include_special.get()

        characters = ''
        if include_alpha:
            characters += string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            self.result_entry.configure(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Please select at least one character type.")
            self.result_entry.configure(state="readonly")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_entry.configure(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, password)
            self.result_entry.configure(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
