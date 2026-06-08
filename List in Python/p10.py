#10.	Write a program to find the second largest element in a list.
lst = [10, 25, 45, 30, 50, 40]

largest = second_largest = float('-inf')

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)