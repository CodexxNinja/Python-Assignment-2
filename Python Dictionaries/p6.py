# Write a program to check whether a given key exists in a dictionary.

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

key = input("Enter key to search: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")
