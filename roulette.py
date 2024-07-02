# This program will ask the user to enter a pocket number and
#display whether the pocket is green, red, or black.
# Jazmin Even Dorra

def main():
    print ("Roulette Wheel Colors App ...")
    #prompt user for pocket number
    pocketNumber = eval(input("Please enter pocket number (0-36): "))

    # if pocket number is 0
    if pocketNumber == 0:
        print ("The Color of the Wheel Pocket is Green")

    # if pocket number is between 1 and 10
    elif pocketNumber >= 1 and pocketNumber <= 10:
        if pocketNumber % 2 == 0:
            print ("The color of the Wheel Pocket is Black")
        else:
            print ("The color of the Wheel Pocket is Red")

    # if pocket number is between 11 and 18
    elif pocketNumber >= 11 and pocketNumber <= 18:
        if pocketNumber % 2 == 0:
            print ("The color of the Wheel Pocket is Red")
        else:
            print ("The color of the Wheel Pocket is Black")

    # if pocket number is between 19 and 28
    elif pocketNumber >= 19 and pocketNumber <= 28:
        if pocketNumber % 2 == 0:
            print ("The color of the Wheel Pocket is Black")
        else:
            print ("The color of the Wheel Pocket is Red")

    # if pocket number is between 29 and 36
    elif pocketNumber >= 29 and pocketNumber <= 36:
        if pocketNumber % 2 == 0:
            print ("The color of the Wheel Pocket is Red")
        else:
            print ("The color of the Wheel Pocket is Black")

    # if pocket number is none of the above
    else:
        print ("\tError ... Invalid pocket. Try again")
    

main()
