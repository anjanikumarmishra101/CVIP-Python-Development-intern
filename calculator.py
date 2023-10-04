import tkinter as tk

def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an Entry widget for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Create a StringVar to display the result
result = tk.StringVar()
result.set("")

# Create a Label to display the result
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=1, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 2, 0
for button in buttons:
    tk.Button(root, text=button, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the '=' button
tk.Button(root, text="=", command=evaluate_expression).grid(row=6, column=0, columnspan=4)

# Start the main loop
root.mainloop()
