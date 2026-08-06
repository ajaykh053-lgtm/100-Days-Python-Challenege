# def add(num_1,num_2):
#     return num_1+num_2

# def sub(num_1,num_2):
#     return num_1-num_2

# def mul(num_1,num_2):
#     return num_1*num_2

# def div(num_1,num_2):
#     return num_1/num_2

# num1=int(input("Enter the number.\n"))
# choice=input("+ --> 'Addition'\n - --> 'Substration'\n * --> 'Multiplication'\n / --> Division\n ")
# num2=int(input("Enter another number.\n"))

# if choice=="+":
#     result=print(add(num1,num2))

# elif choice=="-":
#     result=print(sub(num1,num2))

# elif choice=="*":
#     result=print(mul(num1,num2))

# elif choice=="/":
#     if num2==0:
#         ("Invalid input")
#     else:
#         result=print(div(num1,num2))
# final_result=result
# user_choice=input(f"Do you want to do more calculation with result.\n"
#                    "Type 'yes' to continue or 'no' to see result.\n ").lower()

# while user_choice=="yes":
#     choice=input("+ --> 'Addition'\n - --> 'Substration'\n * --> 'Multiplication'\n / --> Division\n ")
#     num2=int(input("Enter another number.\n"))
#     if choice=="+":
#         result=print(add(final_result,num2))

#     elif choice=="-":
#         result=print(sub(final_result,num2))

#     elif choice=="*":
#         result=print(mul(final_result,num2))

#     elif choice=="/":
#         if num2==0:
#             print("Invalid input")
#         else:
#             result=print(div(final_result,num2))

#     print(f"The result of your calculation is : {result}")

# print(f"The result of your calculation is : {result}")

# def add(n1,n2):
#     return n1+n2

# def subtract(n1,n2):
#     return n1-n2

# def multiply(n1,n2):
#     return n1*n2


# def divide(n1,n2):
#     return n1/n2
# operation={
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }
# # print(operation["*"](4,8))
# num1=int(input("Enter a number : "))
# should_accumlate=True
# while should_accumlate:
#     for symbol in operation:
#         print(symbol)
#     operation_symbol=input("Pick an operation : ")
#     num2=int(input("Enter another number : "))
#     answer=operation[operation_symbol](num1,num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#     choice=input(f"Type 'y' to continue with the calculation with {answer}, or 'n' to see the result : ")
#     if choice=="yes":
#         num1=answer
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    should_accumlate = True
    num1 = int(input("Enter a number : "))
    while should_accumlate:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation : ")
        num2 = int(input("Enter another number : "))
        answer = operation[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(
            f"Type 'y' to continue with the calculation with {answer}, or 'n' to see the result : "
        )
        if choice == "y":
            num1 = answer
        else:
            should_accumlate = False
            print("\n" * 20)
            calculator()


calculator()
