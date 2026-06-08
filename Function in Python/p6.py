#6.Write a function to check whether given year is leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

year = int(input("Enter a year: "))
print(is_leap_year(year))