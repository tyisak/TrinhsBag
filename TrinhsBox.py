#Don't look at this until you run the code!

print("Hi Trinh! To open this bag, you're going to have to find two more enveloples.")

while True:
    answer1 = input("Are you ready? (YES or NO)")
    if answer1 == "YES":
        break
    elif answer1 == "NO": 
        print("Well come back when you are ready then!")
    else: 
        print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

clue1 = "something goes here"
print(clue1)
code1 = "answer1"

while True:
    answer2 = input("What is the first code word?")
    if answer2 == code1:
        break
    else: 
        print("Are you sure you got that right?")

clue2 = "something goes here"
print(clue2)
code2 = "answer2"

while True:
    answer3 = input("What is the second code word?")
    if answer3 == code2:
        break
    else: 
        print("Are you sure you got that right?")

print("Good job, now theres only one thing left to do before you open your bag!  Answer this question:")



while True:
    answer1 = input("Will you be Ty's valentine? (YES or NO)")
    if answer1 == "YES":
        break
    elif answer1 == "NO": 
        print("Don't Hurt my feelings! Try again!")
    else: 
        print("Didn't catch that. Make sure to only answer 'YES' or 'NO'.")

print("I hope you enjoyed the hunt! You can open your bag now. ")

print("Also, dont forget to let me know your answer. <3")


