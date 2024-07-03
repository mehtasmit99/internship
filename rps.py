import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="Rock, Paper, Scissors", font=('Helvetica', 20, 'bold'), bg="#4CAF50", fg="white", pady=10)
        header_label.pack(fill=tk.X)

        # Radio Buttons
        choices = ["Rock", "Paper", "Scissors"]
        ttk.Label(self.root, text="Choose your move:", font=('Arial', 14)).pack(pady=5)
        for choice in choices:
            ttk.Radiobutton(self.root, text=choice, variable=self.user_choice_var, value=choice, style="TRadiobutton").pack(pady=5)

        # Play Button
        play_button = ttk.Button(self.root, text="Play against Robo", command=self.play_game, style="TButton")
        play_button.pack(pady=10)

        # Result Label
        ttk.Label(self.root, text="Result:", font=('Arial', 14)).pack(pady=5)
        result_label = ttk.Label(self.root, textvariable=self.result_var, font=('Arial', 14), foreground="#4CAF50")
        result_label.pack(pady=5)

        # Animation Canvas
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="#ffffff")
        self.canvas.pack(pady=10)
        self.canvas.create_text(100, 100, text="🤖", font=('Arial', 36))

        # Style
        style = ttk.Style()
        style.configure("TButton", background="#4CAF50", font=('Arial', 12), width=20)
        style.map("TButton", background=[('active', '#45a049')])

        style.configure("TRadiobutton", background="#f0f0f0", font=('Arial', 12))

    def play_game(self):
        user_choice = self.user_choice_var.get()

        if not user_choice:
            self.result_var.set("Please choose Rock, Paper, or Scissors.")
            return

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        self.result_var.set(f"Robo chose: {computer_choice}. {result}")

        # Animation
        self.animate_robot()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "You win!"
        else:
            return "You lose!"

    def animate_robot(self):
        for _ in range(3):
            self.canvas.move(1, 20, 0)
            self.root.update()
            self.root.after(300)
        self.canvas.move(1, -60, 0)

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
