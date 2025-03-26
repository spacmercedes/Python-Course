from tkinter import *

window = Tk()
window.title("My GUI")
window.minsize(500,300)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 24,"bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal", font=("Arial", 24,"bold"))
equal_label.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 24,"bold"))
result.grid(column=1, row=1)


km = Label(text="km", font=("Arial", 24,"bold"))
km.grid(column=2, row=1)


#Button
def button_clicked():
    print("click nahui")
    result.config(text=f"{int(input.get()) *1.609}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)







window.mainloop()