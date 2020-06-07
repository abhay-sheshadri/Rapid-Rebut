from tkinter import *
import tkinter.ttk as ttk
from utils.database import *

# GUI Setup
root = Tk()
root.title("RapidRebut Admin") # Sets the title
root.geometry("500x350")
root.resizable(False, False)

# Add two tabs
nb = ttk.Notebook(root)
nb.grid(row=1, column=0, columnspan=40, rowspan=39, sticky="NESW")

page1 = ttk.Frame(nb)
nb.add(page1, text=f'{"Insert": ^20s}')

page2 = ttk.Frame(nb)
nb.add(page2, text=f'{"Remove": ^20s}')

# Insert tab
sv1 = StringVar()
def insert():
    rumor = e1.get("1.0",END).replace("\n", "")
    truth = e2.get("1.0",END).replace("\n", "")
    link = sv1.get()
    add_rumor(rumor, truth, link)
    # Update combobox
    rumors.append(rumor)
    combo["values"] = rumors

WIDTH = 51
l1 = Label(page1, text="Rumor: ")
l1.grid(row=0, column=0)
e1 = Text(page1, width=WIDTH, height=5)
e1.grid(row=0, column=1, padx=10, pady=10)

l2 = Label(page1, text="Correction: ")
l2.grid(row=1, column=0)
e2 = Text(page1, width=WIDTH, height=5)
e2.grid(row=1, column=1, padx=10, pady=10)

l3 = Label(page1, text="Source: ")
l3.grid(row=2, column=0)
e3 = Entry(page1, width=68, textvariable=sv1)
e3.grid(row=2, column=1, padx=10, pady=10)

f3 = ttk.Frame(page1)
f3.grid(row=3,  column=0, columnspan=2)
b1 = ttk.Button(f3, text="Insert Into Database", width=20, command=insert)
b1.grid(row=0, column=0, padx=10, pady=26)

# Remove Tab
def remove():
    r = combo.get()
    delete_rumor(r)
    # Update combobox
    rumors.remove(r)
    combo["values"] = rumors

rumors = get_lists()[0]
combo = ttk.Combobox(page2, width=73, value=rumors)
combo.pack(side="top", padx=15, pady=25)

b2 = ttk.Button(page2, text="Remove From Database", width=24, command=remove)
b2.pack(side="bottom", padx=10, pady=26)

root.mainloop()