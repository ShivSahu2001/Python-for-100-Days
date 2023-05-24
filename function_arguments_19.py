# def average(a,b=8):
#     print("The average is", (a+b)/2)

# average(b=12)

# average(b=14,a=12)

# average(6)

# variable length arguments
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
    # print("The average is: ", sum/len(numbers))
c = average(5,6,7,1)
print(c)


