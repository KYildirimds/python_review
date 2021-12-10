from os import system
from time import sleep
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except:
        print("you can't divide a number by zero")
        for i in range(3,0,-1):
            print(' This warning will be deleted in {} seconds'. format(i))
            sleep(1)
        system('cls')