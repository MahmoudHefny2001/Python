def get_factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        factorial = 1
        for i in range(2, number+1):
            factorial *= i
        return factorial

number = int(input("Enter any number to get its factorial: "))
print(get_factorial(number))