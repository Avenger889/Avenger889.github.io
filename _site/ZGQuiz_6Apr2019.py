#This variable keeps track of the number of questions answered correctly
score = 0

#Introduces the program to the user
print("Welcome to my Quiz!\nI will ask you a series of questions, and tally the amount you answer correctly!")

print()

qone = int(input("Can penguins breathe underwater? (Type '1' for YES, Type '2' for NO)"))

if qone == 2:
    print("Correct! You're quite the zoologist!")
    score += 1
else:
    print("Uh oh! That's not right :/")

print()

qtwo = int(input("Which is healthier, soda or water? (Type '1' for SODA, Type '2' for WATER)"))

if qtwo == 2:
    print("Correct! You know your nutrition!")
    score += 1
else:
    print("Uh oh! That's not right :/")

print()

print("My quiz is over, and you answered", score, "question(s) correctly. Great job!")
