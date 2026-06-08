#9.	Write a program to reverse a list without using built-in reverse functions. 
lst = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])

print("Original List:", lst)
print("Reversed List:", reversed_list)