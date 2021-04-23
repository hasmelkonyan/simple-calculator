def add(number_first, number_second):
    result = number_first + number_second
    return result


def minus(number_first, number_second):
    result = number_first - number_second
    return result


def mul(number_first, number_second):
    result = number_first * number_second
    return result


def div(number_first, number_second):
    try:
        result = number_first / number_second
        number_second = 0
    except ZeroDivisionError:
        print("You can't to divide by zero ")

    return result


print("Hello. This is simple calculator.")
while True:
    try:
        number_first = int(input("input first number"))
        break
    except ValueError:
        print("That is not valid number. try again.")
while True:
    try:
        number_second = int(input("input second number"))
        break
    except ValueError:
        print("That is not valid number. try again.")


operation = input("Yor operation")
if operation == '+':
    print(add(number_first, number_second))
elif operation == '-':
    print(minus(number_first, number_second))
elif operation == '*':
    print(mul(number_first, number_second))
elif operation == '/':
    print(div(number_first, number_second))
else:
    print("Mistake operation")
