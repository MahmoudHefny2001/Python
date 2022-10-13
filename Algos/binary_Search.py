def binary_search(array, item):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = int((low+high)/2)
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
item = int(input("Choose a number to get its index: "))
position = binary_search(numbers, item)
print("Position of "+str(item)+" is: "+ str(position))

