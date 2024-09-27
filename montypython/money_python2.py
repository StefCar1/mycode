#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer != ["shrubbery", "chrubbery" , "shrubery", "shrobbery"]:
    round += 1
    print('In the iconic movie, "Monty Python and the Holy Grail," what did the Knights that say ni ask the travelers to bring them?')
    response = input(" ")
    if response == answer:
        print("Correct!")
    elif round == 1:
        print("Try again!")
    elif round == 2:
        print("You have chosen... poorly.")
    elif round == 3:
        print("The answer was a shrubbery'")
    else:
        print("Bye, bye!")

