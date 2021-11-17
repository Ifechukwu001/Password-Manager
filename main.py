from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    password_list = [choice(letters) for char in range(nr_letters)]
    password_list += [choice(symbols) for symbol in range(nr_symbols)]
    password_list += [choice(numbers) for num in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_input.get()
    username = u_name_input.get()
    pass_word = pass_input.get()
    new_data = {
        website:{
            "email": username,
            "password": pass_word,
        }
    }
    

    if len(website) == 0 or len(pass_word) == 0:
        messagebox.showerror(title="Oops", message="Please make sure no fields are empty!")
    else:
        try:
            with open("_saved_passwords.json", mode="r") as password_data:
                data = json.load(password_data)

        except FileNotFoundError:
            with open("_saved_passwords.json", mode="w") as password_data:
                json.dump(new_data, password_data)

        else:
            data.update(new_data)

            with open("_saved_passwords.json", mode="w") as password_data:
                json.dump(data, password_data, indent=4)

        finally:
            site_input.delete(0, END)
            pass_input.delete(0, END)
            site_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1, column=0)

u_name_label = Label(text="Email/UserName:")
u_name_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

site_input = Entry(width=55)
site_input.focus()
site_input.grid(row=1, column=1, sticky="w", columnspan=2)

u_name_input = Entry(width=55)
u_name_input.insert(0, "ogidiifechukwu@gmail.com")
u_name_input.grid(row=2, column=1, sticky="w", columnspan=2)

pass_input = Entry(width=35)
pass_input.grid(row=3, column=1, sticky="w",)

pass_gen_bttn = Button(text="Generate Password", width=15, command=generate_password)
pass_gen_bttn.grid(row=3, column=2, sticky="w")

submit_bttn = Button(text="Add", width=45, command=save)
submit_bttn.grid(row=4, column=1, sticky="w", columnspan=2)


window.mainloop()