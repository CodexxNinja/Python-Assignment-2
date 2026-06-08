#2.Write a program to find the largest elements in a list.
def find_largest(lst):
    if not lst:
        return None  

    largest = lst[0]  

    for num in lst:
        if num > largest:
            largest = num  

    return largest


numbers = [3, 5, 7, 2, 8]   
largest_number = find_largest(numbers)
print("The largest number in the list is:", largest_number)
    