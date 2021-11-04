from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Project Dice")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


ttk.Label(mainframe, text="Project Dice").grid(column=2, row=1)
ttk.Button(mainframe, text="Login").grid(column=2, row=2)
ttk.Button(mainframe, text="Sign Up").grid(column=2, row=3)
ttk.Button(mainframe, text="Scoreboard").grid(column=2, row=4)
ttk.Frame(mainframe, width=40, height=40).grid(column=1, row=1)
ttk.Frame(mainframe, width=40, height=40).grid(column=3, row=1)
ttk.Frame(mainframe, width=40, height=20).grid(column=2, row=5)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=10)

root.mainloop()
