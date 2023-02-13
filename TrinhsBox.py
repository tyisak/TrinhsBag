#Don't look at this until you run the code!

print("Hi Trinh! To open this bag, you're going to have to find two more enveloples.")

while True:
    answer1 = input("Are you ready? (YES or NO) ")
    if answer1 == "YES":
        break
    elif answer1 == "NO": 
        print("Well come back when you are ready then!")
    else: 
        print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

clue1 = "something goes here"
print(clue1)
code1 = "WILL YOU"

while True:
    answer2 = input("What is the first code? ")
    if answer2 == code1:
        break
    else: 
        print("Are you sure you got that right?")

clue2 = "something goes here"
print(clue2)
code2 = "BE MY"

while True:
    answer3 = input("What is the second code? ")
    if answer3 == code2:
        break
    else: 
        print("Are you sure you got that right?")

print("Good job, now theres only one thing left to do before you open your bag!")

print("This part might be kind of tricky. Based on the last two codes, I need you to guess the final code word. I know it seems impossible but I think you can do it.")

count = 0
while True:
    count = count + 1
    answer1 = input('Whats the code word? HINT: "WILL YOU BE MY ____________? ')
    if answer1 == "VALENTINE":
        break
    else: 
        print("Not quite. Try again!")

if count == 1:
    print("Wow! You got it first try? I never thought you'd figure it out.")

while True:
    answer1 = input("Well now that you know all of the code words... Will you be Ty's valentine? (YES or NO) ")
    if answer1 == "YES":
        break
    elif answer1 == "NO": 
        print("Don't Hurt my feelings! Try again!")
    else: 
        print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

print("I hope you enjoyed the hunt! You can open your bag now. <3 ")



