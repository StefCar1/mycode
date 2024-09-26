#!/usr/bin/env python3
"""script to decide whether the participant is ready to shower"""

def main():
    answer1= input("Would you like to experience taking a shower by someone with ADHD? ")
    if answer1 == "yes":
        answer2 = input("Have you turned the shower on? ")
        if answer2 == "yes":
            answer3 = input("Have you turned the shower knob to the preferred temperature? ")
            if answer3 == "yes":
                answer4 = input("Have you taken your clothes off? ")
                if answer4 == "yes":
                    answer5 = input("Are you ready to step into the shower? ")
                    if answer5 == "yes":
                       # print("Take the damn shower!")
                       answer6 = input("Get in the shower ")
                       if answer6 == "ok":
                           answer7 = input("Is your hair wet enough for shampoo? ")
                           if answer7 == "yes":
                               answer8 = input("Pump some shampoo into your hand. ")
                               if answer8 == "ok":
                                print("You get the drift. This is an example of how tedious and exhausting a simple task can be for neuro-divergent people.")
    else:
        print("Fine! Stay dirty!")

main()
