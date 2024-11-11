import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        # Display the result in the label
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create and place widgets for inputs and operations
label_num1 = tk.Label(app, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(app, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operation = tk.Label(app, text="Choose an operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

# Variable to store the selected operation
operation_var = tk.StringVar(app)
operation_var.set('+')  # Default operation

# Dropdown menu for operation selection
dropdown_operations = tk.OptionMenu(app, operation_var, '+', '-', '*', '/')
dropdown_operations.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(app, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(app, text="Result:")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)