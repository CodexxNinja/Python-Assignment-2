#6.	Write a program to count how many even numbers are present in a list. 

numbers = [10, 15, 20, 25, 30, 35, 40]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Number of even numbers:", count)