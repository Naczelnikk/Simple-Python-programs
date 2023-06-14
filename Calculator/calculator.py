import tkinter as tk

def add(a, b):
    answer = a + b
    result_label.config(text=str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    result_label.config(text=str(a) + " - " + str(b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    result_label.config(text=str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    result_label.config(text=str(a) + " / " + str(b) + " = " + str(answer))

def calculate():
    a = int(entry_a.get())
    b = int(entry_b.get())
    operation = operation_var.get()

    if operation == "Addition":
        add(a, b)
    elif operation == "Subtraction":
        sub(a, b)
    elif operation == "Multiplication":
        mul(a, b)
    elif operation == "Division":
        div(a, b)

root = tk.Tk()
root.title("Calculator")

# Create input fields
label_a = tk.Label(root, text="First number:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Second number:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

# Create operation selection dropdown
operation_var = tk.StringVar()
operation_var.set("Addition")

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.pack()

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
