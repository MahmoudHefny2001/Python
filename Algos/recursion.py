def get_factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * get_factorial(number-1)

number = int(input("Enter any number to get its factorial: "))
print(get_factorial(number))