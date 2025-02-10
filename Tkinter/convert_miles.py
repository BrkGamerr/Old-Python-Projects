from tkinter import *


# Main function that converts from miles to km.
def convert():
    miles = miles_var.get()
    km = miles * 1.6
    result_var.set(km)


# Creates a main window.
window = Tk()
window.title("Mile to Km")
window.geometry("250x75")

# Creates the first label.
length_in_miles = Label(window, text="Miles")
length_in_miles.grid(row=0, column=2)

# Creates the second label.
length_in_km = Label(window, text="is equal to:")
length_in_km.grid(row=1, column=0)

# Creates the third label.
label3 = Label(window, text="Km")
label3.grid(row=1, column=2)

# Creates a button for converting.
button = Button(window, text="Calculate", width=15, command=convert)
button.grid(row=2, column=1)

# Creates input for user.
miles_var = DoubleVar()
user_input = Entry(window, textvariable=miles_var, justify="center")
user_input.grid(row=0, column=1)

# Creates output for result.
result_var = DoubleVar()
result = Entry(window, textvariable=result_var, justify="center")
result.grid(row=1, column=1)

# Keeps the application running.
window.mainloop()
