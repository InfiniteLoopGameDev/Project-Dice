def formatPrint(text):
    for i in range(50):
        print("\n")
    print("Project Dice")
    print("------------------------")
    print(text)


def rollDice():
    import random
    input("Press [Enter] to roll")
    num = random.randint(1, 6)
    print("You rolled a {}".format(num))
    return num


def isEven(x):
    mod = x % 2
    if mod == 0:
        return True
    else:
        return False


def insertLine(lineNum, file, newLine):
    f = open(file, "r+")  # Opens file in read mode
    newLine = "{}\n".format(newLine)  # Formats the newline
    data = f.readlines()  # Stores contents of files as a list
    data.insert(lineNum, newLine)  # Inserts line in the list
    try:
        data.pop(5)  # Removes the 6th score
    except IndexError:
        pass
    f.close()
    f = open(file, "w+")  # Purges the file by opening in write mode
    f.writelines(data)  # Writes list on the file
    f.close()


def pause():
    input("Press [Enter] to continue")
