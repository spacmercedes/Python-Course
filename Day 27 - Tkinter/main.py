from tkinter import *

window = Tk()
window.title("My GUI")
window.minsize(500,300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am label", font=("Arial", 24,"bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

#Entry
input = Entry(width=10)
input.grid(column=5, row=5)


#Button
def button_clicked():
    print("click nahui")
    my_label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="Click Me 2", command=button_clicked)
new_button.grid(column=3, row=0)





window.mainloop()