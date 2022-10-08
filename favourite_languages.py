favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in set(favourite_languages.values()):
    print(language.title())


# friends = ['phil', 'sarah']

# for name in favourite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favourite_languages.keys():
#     print("Erin, please take our poll!")


#for name, language in favourite_languages.items():
   # print(f"{name.title()}'s favorite language is {language.title()}.")

#print()

#for name in favourite_languages.keys():
   # print(name.title())

# sarah_language = favourite_languages['sarah'].title()
# print(f"Sarah's favourite language is {sarah_language}")


favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'noah': ['java', 'c++'],
    'alfred': ['rust'],
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite_languages are: ")
    for language in languages:
        print(f"\t{language.title()}")








































