message = "Hello Python world!"

print(message)

message = "Hello all the puppies!"

print(message)

# print(mesage) Error message is: NameError: name 'mesage' is not defined. Did you mean: 'message'?

name = "ada lovelace"

print(name.title()) #will capitolize the first letter of every word AKA title case
name = "Ada Lovelace"
print(name.upper()) #capitolize all letters
print(name.lower()) #lowercase all letters

#Full Name

first_name = "puppy"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)

message = f"Hello, {full_name.title()}!"

print(message)

print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavascript") # \n is like in C

favorite_language = "    python    "
print(favorite_language)
# favorite_language = favorite_language.rstrip() #gets rid of left white space
# print(favorite_language)

# favorite_language = favorite_language.lstrip() #gets rid of right left space
# print(favorite_language)

favorite_language = favorite_language.strip() #removes whitespace from both sides

print(favorite_language)

# Removing Prefixes

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) #removes the 'https://' from the url but doesn't perminately do so

nostarch_url = nostarch_url.removeprefix('https://') #this lets you keep the removed prefix

#Syntax Errors

message = "One of Python's strengths is its diverse community." #this works
print(message)

# message = 'One of Python's strengths is its diverse community' #this doesn't work Error: SyntaxError: unterminated string literal (detected at line 1)

print('')
print('')
print('')

print('Exercise')

billy = "Hello Billy, would you like to learn some Python today?"
print(billy)

albert = "albert einstein"
albert = albert.title()
print(albert)
albert = albert.lower()
print(albert)
albert = albert.upper()
print(albert)

print('"It is during our darkest moments that we must focus to see the light." \n\t-Aristotle')

famous_person = "Abraham Lincoln"

message = f"'In the end, it's not the years in your life that count. It's the life in your years.' \n\t-{famous_person}"

print(message)

name = "\n\tpuppy\n\t"

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Numbers

universe_age = 14_000_000_000
print(universe_age)
x, y, z = 0, 0, 0

# Multiple Assignment
print(x)
print(y)
print(z)

# Constants

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

print('')
print('')
print('')

print('Exercise')

print(2+6)
print(10-2)
print(2*4)
print(16/2)

fav_number = 9

message = f"My favorite number is {fav_number}"
print(message)

# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# Done!