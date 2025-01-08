import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    try:
        # Get the desired length of the password from the user input
        length = int(entry_length.get())
        
        # Define the characters to be used in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password using random.choice
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        label_password.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a numeric value for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Enter desired password length:").pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
label_password = tk.Label(root, text="Generated Password: ")
label_password.pack(pady=5)

# Start the main event loop
root.mainloop()