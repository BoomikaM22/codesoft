import tkinter as tk

# Function to handle button click and display the value
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the final expression
def equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# Create the main application window
app = tk.Tk()
app.geometry("300x400")
app.title("Calculator")

# Variable to store the input expression
expression = ""

# Variable to store the input expression as a string
input_text = tk.StringVar()

# Create the input field
input_field = tk.Entry(app, textvariable=input_text, font=("Arial", 20, "bold"))
input_field.pack(ipadx=8, pady=10, fill=tk.X)

# Create the buttons for numbers and operations
button_frame = tk.Frame(app)
button_frame.pack()

button_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Add buttons to the button frame
for i in range(4):
    for j in range(4):
        button = tk.Button(button_frame, text=button_list[i*4 + j], padx=15, pady=15, font=("Arial", 12, "bold"),
                           command=lambda x=button_list[i*4 + j]: button_click(x))
        button.grid(row=i, column=j)

# Create the clear button
clear_button = tk.Button(button_frame, text='C', padx=15, pady=15, font=("Arial", 12, "bold"), command=clear)
clear_button.grid(row=4, column=0)

# Create the equal button
equal_button = tk.Button(button_frame, text='=', padx=15, pady=15, font=("Arial", 12, "bold"), command=equal)
equal_button.grid(row=4, column=1, columnspan=2)

# Start the application
app.mainloop()
