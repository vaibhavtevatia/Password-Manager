from tkinter import *
from tkinter import messagebox
import random
import pyperclip3
import json
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip3.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == None or email == None:
        messagebox.showinfo(title = "Error" , message = "FILL THE ENTRIES")

    else:
        try:
            with open("save_file.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("save_file.json", 'w') as file:
                json.dump(new_data, file, indent = 4)

        else:
            data.update(new_data)
            with open("save_file.json", 'w') as file:
                json.dump(data, file, indent = 4)

        finally:
            website_entry.delete(0 ,END)
            password_entry.delete(0 ,END)


def show_password():
    website = website_entry.get()
    email = email_entry.get()
    try:
        with open("save_file.json", "r") as file:
            data = json.load(file)
            password = data[website]["password"]
    except KeyError:
        messagebox.showerror("Unvalid Entries", "Invalid Entry")
    else:
        messagebox.showinfo("Password", f"Password : {password} \n Website : {website} \n For Email : {email}")
        pyperclip3.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx = 50 ,pady = 50)



canvas = Canvas(width = 200, height=  200)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img )
canvas.grid(row = 0 , column =1)

website_label = Label(text = "Website:", font = (FONT_NAME, 7, "bold"))
website_label.grid(row = 1,column=0 )

email_label = Label(text = "Email/Username:", font = (FONT_NAME, 7, "bold"))
email_label.grid(row = 2,column= 0)

password_label = Label(text = "Password:", font = (FONT_NAME, 7, "bold"))
password_label.grid(row =3 ,column= 0)

generate_password_button =Button(text = "Generate Password", highlightthickness = 0, width = 15, command = generate_password)
generate_password_button.grid(row = 3 ,column= 2)

search_button = Button(text = "Search", width = 15, command=  show_password, highlightthickness = 0)
search_button.grid(row =1 , column =2)

add_button = Button(text = "Add", highlightthickness = 0, width = 36, command =save)
add_button.grid(row = 4 ,column= 1, columnspan = 2)

website_entry = Entry(width = 21)
website_entry.grid(row = 1,column= 1)
website_entry.focus()

email_entry = Entry(width = 40)
email_entry.grid(row = 2,column= 1, columnspan = 2)
email_entry.insert(0 ,"v@g.com")

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column =1 )




window.mainloop()
