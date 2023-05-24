
questions = [
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
    [
        "Which language is mostly used for hacking?", "JavaScript","Java" , "Python", "PHP",4
    ],
   
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,520000, 1000000]
moneyGot = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n \n Question for Rs. {levels[i]}")
    print(f"a. {question[1]}   b. {question[2]}")
    print(f"c. {question[3]}   d. {question[4]}")
    reply = int(input("Enter Your answer (1-4)or 0 to quit: "))
    if(reply == 0):
        moneyGot = levels[i - 1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            moneyGot = 10000
        elif(i==9):
            moneyGot = 320000
        elif(i==14):
            moneyGot = 10000000
    else:
        print("Wrong answer! Better Luck next Time")
        break

print(f"Your take home Revenue is {moneyGot}")
