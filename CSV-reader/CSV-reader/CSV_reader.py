from Regex import *
from Maintain_csv_file import *
from tkinter import *
from tkinter import ttk

'''root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Define CSV name: ").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)

define_csv_name = ttk.Entry(root, width=30)
define_csv_name.grid(row=0, column=1)

root.mainloop()
'''

#user_file_choose = input("Hi! Please fill field with your name's file.csv")

Object = MaintainCsvFile()
Object.read_from_csv("Nowy.csv")
Test = Regex()
Test.