import time;

timestamp = time.strftime("%H:%M:%S")
# print(int(timestamp))
print(int(timestamp[0:2]))

if(int(timestamp[0:2]) < 12):
    print("Good Morning")
elif(int(timestamp[0:2]) >= 12 and int(timestamp[0:2]) < 17):
    print("Good Afternoon")
else:
    print("Good Evening")