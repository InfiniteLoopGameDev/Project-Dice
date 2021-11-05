from tkinter import *
from tkinter import ttk
from main import *


def menu_gui():
    root = Tk()
    root.title("Project Dice")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    var = IntVar()
    title = ttk.Label(mainframe, text="Project Dice").grid(column=2, row=1)
    login = ttk.Button(mainframe, text="Login", command=lambda: menu(2)).grid(column=2, row=2)
    sign_up = ttk.Button(mainframe, text="Sign Up", command=lambda: [menu(3), root.destroy()]).grid(column=2, row=3)
    scoreboard = ttk.Button(mainframe, text="Scoreboard", command=lambda: [menu(1), root.destroy()]).grid(column=2, row=4)
    close = ttk.Button(mainframe, text="Close", command=lambda: root.destroy()).grid(column=2, row=5)
    spacer1 = ttk.Frame(mainframe, width=40, height=40).grid(column=1, row=1)
    spacer2 = ttk.Frame(mainframe, width=40, height=40).grid(column=3, row=1)
    spacer3 = ttk.Frame(mainframe, width=40, height=20).grid(column=2, row=6)

    for n in sorted(root.children):
        root.children[n].pack()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=10)

    root.mainloop()

    
def menu(input0):
    while True:
        if input0 == 1:
            scoreboard()
        elif input0 == 2:
            user1, user2 = login()
            if user1 == "" and user2 == "":
                pass
            else:
                game(user1, user2)
        elif input0 == 3:
            sign_up()
            formatPrint("Sign Up Successful! \nPlease Proceed to Login or Sign Up another user")
            pause()



menu_gui()
