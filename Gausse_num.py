# from curses.ascii import isdigit
import random

print("Welcome to the computer game!")
print("Instruction :- You got 10 chance to Gause the Number")

random_number = random.randrange(-1,101)

chance = 0

for i in range (0,11):
    chance +=1
    if chance <=10:
        number = input("Enter Your number : ")
        if number.isdigit():
            number = int(number)
            if int(number) == random_number:
                print("********************************************")
                print("               You won the game!             ")
                print("********************************************")
                break
            else :
                if int(number) <random_number:
                    print("Please! Choose greater number ")
                else :
                    print("Please! Choose lesser number ")
        else :
            print("Enter a number!, Character is not allowed")
    else:
        print("********************************************")
        print("              You lost the game!             ")
        print("********************************************")


