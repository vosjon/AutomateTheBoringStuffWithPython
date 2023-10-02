import random

print("I'm thinking of a number between 1 and 20.")

number = random.randint(1, 20)
count = 0
while True:
    response = int(input("Take a guess:"))
    if response == number:
        count += 1
        if count == 1:
            print(f"Good job! You guess my number in {count} guess.")
            break
        print(f"Good job! You guess my number in {count} guesses.")
        break
    elif response > number:
        print("Your guess is too high.")
        count += 1
    elif response < number:
        print("Your response is too low.")
        count += 1