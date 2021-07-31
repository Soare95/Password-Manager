from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "Email": email_input,
            "Password": password_input
        }
    }

    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Empty Spaces", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete("0", END)
            password_entry.delete("0", END)


def find_password():
    website_input = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This file doesn't exists")
    else:
        if website_input in data:
            email = data[website_input]["Email"]
            password = data[website_input]["Password"]

            messagebox.showinfo(title=f"{website_input}", message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Not Found!", message="No details that the website exists")


window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "soare@email.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons
generate_button = Button(text="Generate Password", width=20, command=generate_password)
generate_button.grid(column=1, row=4, pady=1)

add_button = Button(text="Add", width=20, command=save)
add_button.grid(column=1, row=5, pady=1)

search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(column=1, row=6, pady=1)


window.mainloop()
