
def customer_management():

    print("***************************************************************")
    print("*                    Customer Management                      *")
    print("***************************************************************")
    print("1. New Customer")
    print("2. Print Customers")
    print("3. Search Customer by ID")
    print("B. Back")
    print("E. End")
    option = input("Please, insert a valid option (1-3, E or B): ")

    if option == "1":
        print("You have selected option 1")

        name = input("Please introduce your name: ")
        numbers = ["0", "1,", "2", "3", "4", "5", "6", "6", "7", "8", "9"]
        flag_name = True
        for a in name:
            for p in numbers:
                if a == p:
                    flag_name = False
        if flag_name == False:
            print("You can not enter a number")

        surname = input("Please introduce your surname: ")
        numbers = ["0", "1,", "2", "3", "4", "5", "6", "6", "7", "8", "9"]
        flag_name = True
        for a in surname:
            for p in numbers:
                if a == p:
                    flag_name = False
        if flag_name == False:
            print("You can not enter a number")
        x = 1
        while x != 0:
            ID = input("Please introduce your ID: ")
            if ID[len(ID)-1] == "A":
                x = x-1
            else:
                print("The field has to finish with the letter A")
        x = 1
        while x != 0:
            adress = input("Please introduce your adress: ")
            if len(adress) < 3:
                print("The field must be 3 or more characters")
            else:
                x = x-1
        x = 1
        while x != 0:
            town = input("Please introduce your town name: ")
            if len(town) < 3:
                print("The field must be 3 or more characters")
            else:
                x = x-1
        z = 0
        while z < 9:
            x = 0
            z = 0
            y = 0
            phone = input("Introduce your phone number: ")
            j = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            while x < 9:
                if len(phone) == 9:
                    if y < 10:
                        if j[y] == phone[x]:
                            x = x + 1
                            z = z + 1
                            y = 0
                        else:
                            y = y + 1
                    else:
                        print("The field only accepts numbers")
                        x = x + 9
                else:
                    print("The field has to have 9 numbers")
                    x = x + 9

        print("SUCCESS - the data of the new customer is:")
        print("Name:     ", name)
        print("Surname:  ", surname)
        print("ID:       ", ID)
        print("Adress:   ", adress)
        print("Town:     ", town)
        print("Phone:    ", phone)

    elif option == "2":
        print("You have selected option 2")
    elif option == "3":
        print("You have selected option 3")
    elif option == "E" or option == "e":
        print("You have selected to exit from the customer management menu")
    elif option == "B" or option == "b":
        main_menu()
    else:
        print("Error: invalid option in customer management menu ")


def management_menus(section):
    print("***************************************************************")
    print("*                  " + section +
          " Management Menu                    *")
    print("***************************************************************")
    print("1. New", section)
    print("2. Print", section)
    print("3. Search ", section, " by ID")
    print("B. Back")
    print("E. End")
    option = input("Please, insert a valid option (1-3, E or B): ")

    if option == "1":
        print("You have selected option 1")
    elif option == "2":
        print("You have selected option 2")
    elif option == "3":
        print("You have selected option 3")
    elif option == "E" or option == "e":
        print("You have selected to exit from the sensor management menu")
    elif option == "B" or option == "b":
        main_menu()
    else:
        print("Error: invalid option in sensor management menu ")


def main_menu():

    print("***************************************************************")
    print("*                          Main Menu                          *")
    print("***************************************************************")
    print("1. Customer Management")
    print("2. Sensor Management")
    print("3. Security System Management")
    print("4. Sales Management")
    print(" ")
    print("E. End")
    print("")

    option = input("Please, insert a valid option (1-4, E or B): ")

    if option == "1":
        customer_management()

    elif option == "2":
        management_menus("sensor")

    elif option == "3":
        management_menus("systems")

    elif option == "4":
        management_menus("sales")

    elif option == "E" or option == "e":
        print("You have selected to exit from the main menu")
    else:
        print("Error: invalid option in main menu ")
        main_menu()


main_menu()
