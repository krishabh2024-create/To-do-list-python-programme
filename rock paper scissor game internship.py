import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Determine winner
def determine_winner(user_choice):
    comp_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x400")
root.resizable(False, False)

# Title
tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold")).pack(pady=20)

# Labels for user and computer choices
user_label = tk.Label(root, text="You chose: ", font=("Helvetica", 14))
user_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 14))
comp_label.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
result_label.pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=12, command=lambda: determine_winner("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=12, command=lambda: determine_winner("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=12, command=lambda: determine_winner("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()
