#7.	Write a program to create a new list containing only the odd numbers from an existing list. 

numbers = [10, 15, 22, 33, 40, 55, 67, 80]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Original List:", numbers)
print("Odd Numbers List:", odd_numbers)