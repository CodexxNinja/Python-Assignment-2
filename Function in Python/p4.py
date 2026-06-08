#4.Write a function to check whether a person is eligible to vote or not. (age>=18 )
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible to vote."
    else:
        return "Not eligible to vote."

age = int(input("Enter your age: "))
print(check_voting_eligibility(age))