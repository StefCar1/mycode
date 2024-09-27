#!/usr/bin/env python3

affirmative = ["yes", "Yes", "YES", "affirmative" ,"Affirmative", "AFFIRMATIVE", "I guess", "I Guess", "I GUESS", "sure", "Sure", "SURE", "yah", "Yah", "YAH", "yeah", "Yeah", "YEAH"]
negative = ["no", "No", "NO", "negative", "Negative", "NEGATIVE", "HELL NO"]

print("Welcome to the free things to do questionnaire!")
answer = input("Do you want to go outside? ")
if answer in affirmative:
    answer = input("Are you feeling adventurous? ")
    if answer in affirmative:
        answer = input("Would you like to go on a hike sound? ")
        if answer in affirmative:
            answer = print("Awesome! I'll see you on the trail! ")
        if answer in negative:
            answer = input("Does the beach sound like a plan? ")
            if answer in affirmative:
                print("Let me grab my beach towel and flipflops!")
            if answer in negative:
                answer = input("Let's go for a bikeride! ")
                if answer in affirmative:
                    print("Remember your helmet!")
                if answer in negative:
                    print(" I wish I could find something else for you. ")
    if answer in negative:
        answer = input("Does people watching sound fun? ")
        if answer in affirmative:
            place = input("where's the best place to people watch? ")
            print(f"Bet strange people hangout at {place}!")
elif answer in  negative:
    print("Nothing wrong with relaxing at home! ")
    answer = input("Are you up to date on your shows? ")
    if answer in  affirmative:
        print("You could always start on that Start Trek marathon you promised yourself a while back. ")
        answer = input("Do you have any shows you've wanted to watch? ")
        if answer in affirmative:
            show = input("Which show is that? ")
            print(f"I hope you enjoy {show}! ") 
else:
    print("Nothing wrong with spending money for fun! ")    
    answer = int(input("How much money do you feel like spending? "))
    if money >= 30:
        print(f"There is quite a bit you could do with {money}!")
        want = input("You could go out to eat with a friend, take a drive, go see a movie, visit a museam and more! Which of these sound interesting to you? ")
        if want == ["eat", "out", "friend"]:
            print("That's a great way to socialize! Have fun!")
        if want == "drive":
            print("Drive's are akways great to clear your head!")

