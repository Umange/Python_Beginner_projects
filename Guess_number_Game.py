from random import randint
lower_number , Higher_number = 1,5
random_number = randint(lower_number,Higher_number)
print(f" Guess the number in the range from {lower_number} to {Higher_number}  ")
while True :
    try :
        user_input = int(input(("Guess : ")))

    except ValueError as e:
        print("Please enter corrct value :) ")
        continue

    if user_input > random_number:
        print(f" your entered number is higher number Please Enter again for Matching ")

    elif user_input < random_number:
        print(f" your entered number is lower number Please Enter again for Matching ")
    else:
        print("Yay! You Guess It !")
        break