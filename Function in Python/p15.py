#15.Write a function that accepts a number n and returns the sum of all numbers from 1 to n.
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total    

n = int(input("Enter a number: "))
print(f"The sum of all numbers from 1 to {n} is: {sum_of_numbers(n)}")