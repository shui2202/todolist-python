from tkinter import *
import tkinter.messagebox
from tkmacosx import Button


window = Tk()
window.title("Todo list")
window.resizable(False, False)
window.geometry("550x700")

def add_item():
    items = item.get()
    if items != "":
        listbox_items.insert(END, items)
        item_entry.delete(0, END)
    else:
        tkinter.messagebox.showerror(title = "Error", message = "Type something in!")
    

def remove_item():
    item_index = listbox_items.curselection()
    listbox_items.delete(item_index)




add = Button(window, text = "Add", command = add_item, bg = "#00FF00", font = ("Futura", 10, "bold"), borderless = True)
add.place(x = 80, y = 650)

remove = Button(window, text = "Remove", command = remove_item, bg = "#ff0000", font = ("Futura", 10, "bold"), borderless = True)
remove.place(x = 350, y = 650)


item = StringVar()

item_entry = Entry(textvariable = item, width = 70, font = ("Futura", 10))
item_entry.place(x = 20, y = 15)

listbox_items = Listbox(window, height = 34, width = 55)
listbox_items.place(x = 22, y = 50)

window.mainloop()