import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice
def play(user_choice):
    # Generate a random choice for the computer
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display the result
    label_result.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create and place the widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=10)

tk.Button(root, text="Rock", command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack(pady=5)

label_result = tk.Label(root, text="Your choice: \nComputer's choice: \nResult: ")
label_result.pack(pady=10)

# Start the main event loop
root.mainloop()