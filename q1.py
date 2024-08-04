def count_vowels_consonants(string1):
    vowels = "aeiou"
    cons_count = 0
    vowel_count = 0

    for char in string1:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                cons_count += 1

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", cons_count)

# Get input from user
string1 = input("Enter a string: ")
count_vowels_consonants(string1)