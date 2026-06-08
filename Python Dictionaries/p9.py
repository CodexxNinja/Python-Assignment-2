# Write a program to iterate through a dictionary and print all keys and their corresponding values.

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

for key, value in student.items():
    print(key, ":", value)
