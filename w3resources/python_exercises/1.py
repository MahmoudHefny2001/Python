#Write a Python program that find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

def is_numbers_in_list(numbers, number1, number2):
    number1_list = []
    number2_list = []
    for number in numbers:
        if number == number1:
            number1_list.append(number)

        elif number == number2:
            number2_list.append(number)

        else:
            continue

    if len(number1_list) == 2 and len(number2_list) >= 3:
        return True

    return False

numbers = [19, 19, 15, 5, 3, 5, 5, 2]
numbers2 = [19, 15, 15, 5, 3, 3, 5, 2]
numbers3 = [19, 19, 5, 5, 5, 5, 5]

value = is_numbers_in_list(numbers, 19, 5)
print(value)

value = is_numbers_in_list(numbers2, 19, 5)
print(value)

value = is_numbers_in_list(numbers3, 19, 5)
print(value)

print()
#
"""W3Resource Solution"""
#
print()

def check(numbers):
    return numbers.count(19) == 2 and numbers.count(5) >= 3

numbers = [19, 19, 15, 5, 3, 5, 5, 2]

print("Original list: ")
print(numbers)

print("Check two ocurrences of nineteen and at least three occurrences of five in the list")
print(check(numbers))

numbers = [19, 15, 15, 5, 3, 3, 5, 2]
print("\nOriginal list: ")
print(numbers)

print("Check two occurrences of nineteen and at least three occurrences of five in the list")
print(check(numbers))

numbers = [19, 19, 5, 5, 5, 5, 5]
print("\nOriginal list: ")
print(numbers)
print("Check tow occurrences of nineteen and at least three occurrences of five in the list")
print(check(numbers))

































