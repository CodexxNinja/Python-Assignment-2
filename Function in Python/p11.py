#11.Write a function to calculate and return the square of a number.
def square(num):
    return num ** 2

num = int(input("Enter a number: "))
print(f"The square of {num} is {square(num)}.")
