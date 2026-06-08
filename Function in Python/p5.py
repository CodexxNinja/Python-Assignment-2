#5.Write a function to whether a number is divisible by 5 or not.
def is_divisible_by_5(num):
    if num % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 5"

num = int(input("Enter a number: "))
print(is_divisible_by_5(num))
