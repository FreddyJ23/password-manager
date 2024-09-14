from tkinter import *
from tkinter import messagebox
import pyperclip
import random
WHITE = "white"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
           'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator


def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters_list = [random.choice(LETTERS) for _ in range(nr_letters)]
    random_numbers_list = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    random_symbols_list = [random.choice(NUMBERS) for _ in range(nr_numbers)]

    password_list = random_letters_list + random_numbers_list + random_symbols_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="opps", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {email} \n"
                                                      f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                web_input.delete(0, "end")
                password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=pass_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", bg=WHITE)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:  ", bg=WHITE)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:  ", bg=WHITE)
password_label.grid(column=0, row=3)

# Entries
web_input = Entry(width=50)
web_input.grid(column=1, row=1, columnspan=2, sticky=W)
web_input.focus()

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2, sticky=W)
email_input.insert(0, "freedomochulor22@gmail.com")
password_input = Entry(width=31)
password_input.grid(column=1, row=3, sticky=W)

# Buttons
pass_button = Button(text= "Generate Password", highlightthickness=0, width=13, command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=42, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)




window.mainloop()