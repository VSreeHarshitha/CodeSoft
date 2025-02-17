import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# GUI Setup
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x350")
app.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(app, text="Simple Calculator", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Entry Fields for Numbers
entry1 = tk.Entry(app, width=20)
entry1.pack(pady=5)
entry2 = tk.Entry(app, width=20)
entry2.pack(pady=5)

# Operation Selection
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation

operation_frame = tk.Frame(app)
operation_frame.pack(pady=5)

tk.Label(operation_frame, text="Select Operation:", bg="#f0f0f0").pack(side="left")
tk.OptionMenu(operation_frame, operation_var, "+", "-", "*", "/").pack(side="left")

# Calculate Button
calculate_button = tk.Button(app, text="Calculate", command=calculate, bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="Result: ", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the application
app.mainloop()
