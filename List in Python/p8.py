#8.	Write a program to find whether a given element exists in a list. 
lst = [10, 20, 30, 40, 50]

element = int(input("Enter element to search: "))

if element in lst:
    print("Element exists in the list")
else:
    print("Element does not exist in the list")