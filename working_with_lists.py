magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show.")

# for magician in magicians: # IndentationError: expected an indented block after 'for' statement on line 9
# print(magician)

# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# ❶ print(f"I can't wait to see your next trick, {magician.title()}.\n") #SyntaxError: invalid character '❶' (U+2776), but apparently typically doesn't give an error

# message = "Hello Python world!"
#     print(message) # IndentationError: unexpected indent

# for magician in magicians #SyntaxError: expected ':'
#     print(magician)

pizzas = ['pepparoni', 'supreme', 'veggie', 'cheese']

for pizza in pizzas:
    print(f"I like {pizza} pizzas")

print('I really love pizzas.')

pets = ['dog', 'cat', 'tortoise']

for pet in pets:
    print(f'{pet.title()}s make good pets.')

print('Any of these make good pets.')

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))

print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# test = list(range(2, 10, 3)) # the 3rd number is what the number is multiplied by, 1st is where it starts, 2nd is where it should end
# print(test)

squares = []

for value in range(1, 11):
    square = value ** 2 # remember, ** is the power 'symbol'
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

for value in range(1, 21):
    print(value)

one_million = []

# for value in range(1, 1_000_001):
#     one_million.append(value)

# print(min(one_million))
# print(max(one_million))
# print(sum(one_million))

for value in range(2, 21, 2):
    print(value)

for value in range(3, 31, 3):
    print(value)

for value in range(1, 11):
    cubed = value ** 3
    print(cubed)

# Slicing List

players = ['charles', 'martina', 'michael', 'forence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# friend_foods = my_foods #this doesn't work, you must have it in square brackets

print("My favorite foods are:")
print(my_foods)

my_foods.append('cannoli')

friend_foods.append('ice cream')
print('')

print("My favorite foods are:")
print(my_foods)
print('')

print("My friend's favorite foods are:")
print(friend_foods)

print(f"The first three items in the list are: {players[1:4]}")

print(f"Three items from the middle of the list are: {digits[3:6]}")

friend_pizza = pizzas[:]
friend_pizza.append('hawaiian')

print(f"My favorite pizzas are: {pizzas}")
print(f"My friend's favorite pizzas are: {friend_pizza}")

dimensions = (200, 50)
# dimensions[0] = 250 #throws error: TypeError: 'tuple' object does not support item assignment
print(dimensions[0])
print(dimensions[1])

my_t = (3, )
print(my_t)

print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)

#read through this: https://python.org/dev/peps/pep-0008

