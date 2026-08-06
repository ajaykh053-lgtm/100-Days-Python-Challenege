# try:
#     age=int(input("how old are you? "))
# except ValueError:
#     print("You have typed in an invalid value. Please enter a numerical value such as 2.")
#     age=int(input("how old are you? "))
# if age>18:
#     print(f"You can drive at age {age}")


def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(100)
