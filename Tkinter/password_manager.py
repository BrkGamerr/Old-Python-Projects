import password_generator as pg
import json
from tkinter import *
from tkinter import messagebox


# Generates a random password and inserts it into the Entry widget.
def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, pg.generate_password())


# A function to clear user input after clicking the "Add" button.
def clear_entry():
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)


# Main function to add user inputs to .txt file.
def add_new_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }
    if website == "" or email_username == "" or password == "":
        messagebox.showwarning("Warning", "Please don't leave any fields empty!")
    else:
        try:
            with open("day_29_data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("day_29_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("day_29_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                clear_entry()


# Creates a main window.
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

# Creates the canvas to import a picture.
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="password_manager_logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Creates labels.
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Using .grid() to place Label widgets.
website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Declares variable types for Entry inputs.
website_var = StringVar()
email_username_var = StringVar()
password_var = StringVar()

# Creates inputs for user.
website_entry = Entry(textvariable=website_var)
website_entry.focus()  # When you run the code, the cursor is within the website entry box.
email_username_entry = Entry(textvariable=email_username_var)
password_entry = Entry(textvariable=password_var)

# Using .grid() to place Entry widgets.
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry.grid(row=3, column=1, sticky="EW")

# Creates buttons.
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=35, command=add_new_data)

# Using .grid() to place Button widgets.
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# Keeps the application running.
window.mainloop()
