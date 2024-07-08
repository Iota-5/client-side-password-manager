from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = [choice(letters) for _ in range(randint(8, 10))]
    sym = [choice(symbols) for _ in range(randint(2, 4))]
    num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = let + sym + num

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def log_data():
    new_data = {
        website_input.get().title(): {
            "email": user_input.get(),
            "password": password_input.get(),
        }
    }

    if website_input.get() == "" or user_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="error", message="Please fill in all fields")
    else:
        try:
            with open("user_data.json", "r") as data_file:
                # loads data
                data = json.load(data_file)
                # updates data to RAM
                data.update(new_data)
                # saving updated data to permanent place

        except (FileNotFoundError, json.JSONDecodeError):
            data = new_data


        with open("user_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def find_website():
    try:
        with open("user_data.json", "r") as data_file:
            # loads data
            data = json.load(data_file)
            email = data[website_input.get().title()]["email"]
            user_pass = data[website_input.get().title()]["password"]
            messagebox.showinfo(f"{website_input.get().title()}", f"Email: {email} \n"
                                                                               f" Password: {user_pass}")
    except (KeyError, json.JSONDecodeError):
        messagebox.showinfo("error", "This website does not exist in the database.")


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Password Manager")
screen.config(padx=40, pady=40)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()

user = Label(text="Email/Username:")
user.grid(row=2, column=0)

user_input = Entry(width=35)
user_input.grid(row=2, column=1, columnspan=2, sticky="ew")
user_input.insert(0, "test_email@404.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=33)
password_input.grid(row=3, column=1)

password_generator = Button(text="Generate Password", command=gen_password, width=15)
password_generator.grid(row=3, column=2)

add = Button(text="add", width=30, command=log_data)
add.grid(row=4, column=1, columnspan=2, sticky="ew")

search = Button(text="Search", command=find_website, width=15)
search.grid(row=1, column=2)

screen.mainloop()
