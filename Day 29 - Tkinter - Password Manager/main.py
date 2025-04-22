from tkinter import *
from tkinter import messagebox
import json

import random
#--------------------------------------------
# DAY 5 - Password Generator - My Version
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= [random.choice(letters) for _ in range(random.randint(8,10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    finalPassword = ''


    passLetters = nr_letters + nr_symbols + nr_numbers
    random.shuffle(passLetters)

    for letter in passLetters:
        finalPassword += letter

    password_entry.insert(0, finalPassword)



#----------------------------------------

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You got empty fields.")
    else:
            try:
                with open("data.json", "r") as data_file:
                    # json.dump(new_data,data_file, indent=4)
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file,indent=4)
                    #Updating old data
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                #Saving old data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0, END)

#-----------------------------FIND PASSWORD------------------------------

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No such data miss girl." )


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=400, width=400)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200,200, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)



website_entry = Entry(width=50)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=70)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0,"email@mail.com")
password_entry = Entry(width=52)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width= 15, command=find_password)
search_button.grid(column=2 , row=1)
generate_password_button  = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=60, command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
