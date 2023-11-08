name = input("Please introduce your surname: ")
numbers= ["0","1,","2","3","4","5","6","6","7","8","9"]
flag_name= True
for a in name:
    for p in numbers:
            if a == p:
                flag_name= False
if flag_name== False:
     print("You can not enter a number")