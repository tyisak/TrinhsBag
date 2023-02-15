#Don't look at this until you run the code!

def trinhsbox():
    print("Hi Trinh! To open this bag, you're going to have to find two more enveloples.")

    while True:
        answer1 = input("Are you ready? (YES or NO) ")
        if answer1 == "YES":
            break
        elif answer1 == "NO": 
            print("Well come back when you are ready then!")
        else: 
            print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

    clue1 = "The location of the first code is in the place where you asked me to be your boyfriend... gross."
    print(clue1)
    code1 = "WILL YOU"

    while True:
        answer2 = input("What is the first code? ")
        if answer2 == code1:
            print('Correct!')
            break
        else: 
            print("Are you sure you got that right?")

    clue2 = "The location of the second code is your favorite thing to steal. Something you'll probably be doing again soon. "
    print(clue2)
    code2 = "BE MY"

    while True:
        answer3 = input("What is the second code? ")
        if answer3 == code2:
            print('Correct!')
            break
        else: 
            print("Are you sure you got that right?")

    print("Good job, now theres only one thing left to do before you open your bag!")

    print("This part might be kind of tricky. Based on the last two codes, I need you to guess the final code word.")
    print("I know it seems impossible but I think you can do it.")
    count = 0
    while True:
        count = count + 1
        answer1 = input('Whats the code word? HINT: "WILL YOU BE MY ____________? ')
        if answer1 == "VALENTINE":
            print('Correct!')
            break
        else: 
            print("Not quite. Try again!")

    if count == 1:
        print("Wow! You got it first try? I never thought you'd figure it out.")

    print("Well now that you know all of the code words... ")

    while True:
        answer1 = input("Will you be Ty's valentine? (YES or NO) ")
        if answer1 == "YES":
            break
        elif answer1 == "NO": 
            print("Don't Hurt my feelings! Try again!")
        else: 
            print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

    print("I hope you enjoyed the hunt! You can open your bag now. <3 ")



