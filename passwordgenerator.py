import tkinter as tk
import random
import string

def generate_password():
    password_length = length_var.get()
    if password_length > 0:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(password_length))
        password_var.set(password)
    else:
        password_var.set("Password length should be greater than 0.")

app = tk.Tk()
app.title("Password Generator")
app.geometry("300x200")


length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)

length_var = tk.IntVar()
length_entry = tk.Entry(app, textvariable=length_var)
length_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(app, textvariable=password_var, show="*")
password_entry.pack(pady=5)

app.mainloop()
