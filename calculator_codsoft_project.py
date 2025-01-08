import tkinter as tk
from tkinter import messagebox

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

tk.Label(root, text="Select operation:").pack(pady=5)
operation_var = tk.StringVar(value="Add")
tk.Radiobutton(root, text="Add", variable=operation_var, value="Add").pack()
tk.Radiobutton(root, text="Subtract", variable=operation_var, value="Subtract").pack()
tk.Radiobutton(root, text="Multiply", variable=operation_var, value="Multiply").pack()
tk.Radiobutton(root, text="Divide", variable=operation_var, value="Divide").pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=5)

# Start the main event loop
root.mainloop()