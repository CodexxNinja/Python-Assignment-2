#10.Write a function that print multiplication table of a given number.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

number = int(input("Enter a number: "))
multiplication_table(number)
