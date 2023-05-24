def func1():
    try:
        l = [2, 4, 7, 5]
        i = int(input("Enter a number: "))
        print(l[i])
        return 1
        
    except:
        print("Some error occured")
        return 0

    finally:
        print("always executed!!")
        # print("Always executed!!")

x = func1()
print(x)