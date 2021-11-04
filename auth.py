from funcs import *


def login():
    try:
        f = open("auth.csv", "r+")  # Open the CSV storing the usernames and passwords in read-only mode
    except FileNotFoundError:
        print("Please sign up first!")
        pause()
        return("", "")
    found1 = False
    found2 = False

    while not found1:  # Checks if the user is successfully logged in
        user1 = str(input("Enter Player 1 username: "))
        pass1 = str(input("Enter Player 1 password: "))
        userpass1 = user1 + ", " + pass1 + "\n"
        for line in f.readlines():  # Moves the read-head down a line
            if(line == userpass1):  # Checks if current line is the same as the username and password
                print("\nWelcome, " + user1 + "\n")
                found1 = True  # Declares the user as logged in
                break  # Stops the program for searching further down the list
        if not found1 :
            print("\nPlease try again\n")
            f.seek(0)  # Sets the read-head to the start of the file

    while not found2:  # Repeates process for the second user
        f.seek(0)  # Sets the read-head to the start of the file
        user2 = input("Enter Player 2 username: ")
        pass2 = input("Enter Player 2 password: ")
        userpass2 = user2 + ", " + pass2 + "\n"
        for line in f.readlines():
            if(line == userpass2) and (userpass2 != userpass1):
                print("\nWelcome, " + user2 + "\n")
                found2 = True
                break
        if not found2 and (userpass2 == userpass1):  # Checks if the second user is the same as the first
            print("Player 2 cannot be the same as Player 1")
            f.seek(0)
        elif not found2 :
            print("\nPlease try again\n")
            f.seek(0)

    return(user1, user2)  # Sends the name of both users to the main program


def signUp():
    f = open("auth.csv", "a+")  # Open the CSV storing the usernames and passwords in read mode to verify the username hasn't already been used
    Valid = False
    Valid2 = True

    while not Valid:
        user = str(input("Enter Desiered Username: "))
        passw = str(input("Enter Desiered Password: "))
        userpass = user + ", " + passw + "\n"
        for line in f.readlines():  # Moves the read-head down a line
            temp = line.split(",")  # Splits the username-password combination
            userline = temp[0]  # Removes the password
            if(userline == user):  # Compares the chosen username with the existing one
                print("Desiered Username is already user")
                Valid = False
                Valid2 = False
                f.seek(0)
                break
            else:
                Valid2 = True
        if Valid2:
            f.close()
            f = open("auth.csv", "a")  # Switches to file append mode
            f.write(userpass)  # Appends chosem username-password combination
            Valid = True

