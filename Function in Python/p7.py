#7.Write a function to check a whether a character is a vowel or consonant.
def check_vowel_consonant(char):
    if char in 'aeiouAEIOU':
        return "Vowel."
    elif char.isalpha():
        return "Consonant."
    else:
        return "Not an alphabetic character."   
# 
character = input("Enter a character: ")
print(check_vowel_consonant(character))