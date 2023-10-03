def collatz(number):
    try:

        if number % 2 == 0:
            print(number // 2)
            return number // 2
        else:
            result = 3 * number + 1
            print(result)
            return result
        collatz(number)
    except ValueError:
        print("Please enter an interger")

number = int(input("Please enter a number: "))
while number != 1:
    number = collatz(number)