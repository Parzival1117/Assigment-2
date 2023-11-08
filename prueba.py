z = 0
while z == 0:
    x = 0
    y = 0
    name = input("Introduce your name:")
    j = ("0123456789")
    while x < len(name):
        if y < 10:
            if j[y] == name[x]:
                print("The field only accepts letters")
                x = x+len(name)
            else:
                y = y+1
        else:
            x = x+1
            y = 0
        if len(name) == x:
            z = 1

z = 0
while z == 0:
    x = 0
    y = 0
    surname = input("Introduce your surname: ")
    j = "0123456789"
    while x < len(surname):
        if y < 10:
            if j[y] == surname[x]:
                print("The field only accepts letters")
                x = x + len(surname)
            else:
                y = y + 1
        else:
            x = x + 1
            y = 0
        if len(surname) == x:
            z = 1
