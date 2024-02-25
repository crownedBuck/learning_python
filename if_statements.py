# Conditional Tests

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Ignoring case when checking for equality, use .lower()

#Checking for Inequality

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("")
    print("Hold the anchovies!")
    print("")

#Numerical Comparisons

age = 18
if age == 18:
    print(True)

answer = 17
if answer != 42: #you can also use the other mathmatical comparisons
    print("That is not the correct answer. Please try again!")

# Checking Multiple Conditions

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

# Using or to Check Multiple Conditions

age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18

print(age_0 >= 21 or age_1 >= 21)

#Checking Wheather a Value Is in A List

requested_topping = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_topping)

print('pepperoni' in requested_topping)

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

dog_name = 'ghost'
print("Is dog_name == 'ghost'? I predict True")
print(dog_name == 'ghost')
print('')

print("Is dog_name == 'luna'? I predict False")
print(dog_name == 'luna')

# If Statements

# Basic if statment:
#if condtional_test:
#   do something

age = 19
if age >= 18:
    print("\nYou are old enough to vote")
    print("Have you registered to vote yet?")

#If-else Statemetns

age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")

#If-elif-else Chain

age = 12

if age < 4:
    # print("Your admission cost is $0.")
    price = 0
elif age < 18:
    # print("Your admission cost is $25.")
    price = 25
else:
    # print("Your admission cost is $40.")
    price = 40

print(f"Your admission cost is ${price}.")

# Using Multiple elif Blocks

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"\nYour admission cost is ${price}.")

# Omitting the else Block


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20

print(f"\nYour admission cost is ${price}.")

#Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print("\nFinished making your pizza!")

alien_color = 'green'



if alien_color == 'green':
    print("\nYou just earned 5 pts!")
if alien_color == 'yellow':
    print("\nYou just earned 10 pts!")
if alien_color == 'red':
    print("\nYou just earned 15 pts!")

if alien_color == 'green':
    print("\nYou just earned 5 pts!")
elif alien_color == 'yellow':
    print("\nYou just earned 10 pts!")
elif alien_color == 'red':
    print("\nYou just earned 15 pts!")

age = 37

if age < 2:
    print("They're a baby.")
elif age >= 2 and age < 4:
    print("They're a toddler.")
elif age >= 4 and age < 13:
    print("They're a kid.")
elif age >= 13 and age < 20:
    print("They're a teenager.")
elif age >= 20 and age < 65:
    print("They're an adult.")
else:
    print("They're an older adult.")

favorite_fruits = ['pears', 'watermelons', 'blood oranges', 'apple']

for fruit in favorite_fruits:
    if fruit == "apple":
        print("You really like apples!")
    elif fruit == "raspberry":
        print("You really like raspberries!")
    elif fruit == "blood oranges":
        print("You really like blood oranges!")

#If Statements with Lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    # print(f"Adding {requested_topping}.")
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?\n")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

usernames = ['madoka', 'kyuubyi', 'admin', 'blackWeb', 'recluise']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?\n\n')
    else:
        print(f'Hello {username}, thank you for logging in again.\n\n')

# usernames = []

if usernames == []:
    print("We need to find some users!")

# current_users = ['blackWeb', 'recluise']

print([username.lower() for username in usernames])

lowercase_usernames = [username.lower() for username in usernames]

new_users = ["pickleRick", "blackWeb"]

for user in new_users:
    # print(f'{user.lower()} == {lowercase_usernames}')
    if user.lower() in lowercase_usernames:

        print(f"please enter a new username as that one is in use: {user.lower()}")

# Styling Your if Statements

# Make sure you give adequate space