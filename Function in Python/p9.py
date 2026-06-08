#9.Write a function to calculate sum of numbers from 1 to 100.
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print("The sum is:",sum_of_numbers(100))