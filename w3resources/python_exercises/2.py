"""
    Write a python program that accept a list of integers and check the length and the fifth element.
    Return True if the lenght of the list is 8 and the fifth element occurs thrice in the said list.

"""

def check(numbers):
    targeted_number = numbers[4]
    if len(numbers) == 8 and numbers.count(targeted_number) == 3:
        return True
    return False


numbers = [19, 19, 15, 5, 5, 5, 1, 2]
value = check(numbers)

numbers = [19, 15, 5, 7, 5, 5, 2]
value = check(numbers)

print(numbers)
print(value)


