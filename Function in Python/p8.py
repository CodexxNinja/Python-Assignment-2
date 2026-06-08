#8.Write a function to find largest among three numbers.
def largest(a,b,c):
    if a>b and a>c:
        return "a is largest"
    elif b>a and b>c:
        return "b is largest"
    else:
        return "c is largest"

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
c=int(input("Enter third number: "))
print(largest(a,b,c))