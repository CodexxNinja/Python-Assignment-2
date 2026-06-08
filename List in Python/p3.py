#3.	Write a program to find the smallest element in a list. 
def find_smallest_element(lst):
    if not lst:
        return None  

    smallest = lst[0]  

    for num in lst:
        if num < smallest:
            smallest = num  

    return smallest

numbers = [5, 2, 9, 1, 5, 6 ]
smallest_element = find_smallest_element(numbers)   
print("The smallest number in list is:",smallest_element)