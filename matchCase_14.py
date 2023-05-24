num = int(input("Enter the value of num: "))
# num is the variable to match
# similar to switch case
match num:
    case 0:
        print("num is 0")
    case 4:
        print("num is 4")
        
        #default case
    case _:
        print(num)