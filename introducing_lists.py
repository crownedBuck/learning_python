# Lists

bicycles = ['treck', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[0]) #like every other language I've learned so far. 

print(bicycles[0].title())

# Index Positions Start at 0 not one, like every other language I know

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1]) #ALWAYS return last item on the list. This syntax is new as most languages would return an error. At least from the ones I know

message = f"My first bicycle was a {bicycles[0].title()}"

print(message)

print('')
print('')
print('')

print('Exercise')

name = ['Mark', 'Sarah', 'Seth', 'Pickles']
print(name[0])
print(name[1])
print(name[2])
print(name[3])

car = ['Porche', 'Astin Martin', 'Impalla']

message = "I would like to own a"

mes = f"{message} {car[0]}"
print(mes)

mes =f"{message} {car[1]}"
print(mes)

mes = f"{message}n {car[2]}"
print(mes)

# Modifying, Adding, and Removing Elements

# Modifying

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles[0] = 'ducati' #easy enough to change
# print(motorcycles)

# motorcycles.append('ducati') #adds items to the ends of lists
# print(motorcycles)

# motorcycles.insert(0, 'ducati') #adds items to where you tell it to put it
# print(motorcycles)

# del motorcycles[0] #deletes items in place 0
# print(motorcycles)

# popped_motorcycle = motorcycles.pop() #removes item at the end and puts it into popped_motorcycle if you do it like this
# print(motorcycles)
# print(popped_motorcycle)


first_owned = motorcycles.pop(0) #removes item at place 0 and puts it into first_owened var
print(f"The first motorcycle I owned was a {first_owned.title()}")
# motorcycles.remove('ducati') #if there are more than one of the same item in the list, will need to loop through list to remove them all
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print('')
print('')
print('')

print('Exercise')
print('')

invited_to_dinner = ['Harriet Tubman', 'Boudica', 'Grandma Hart', 'Ada Lovelace', 'Grace Hopper', 'Sirimavo Bandaranaike', 'Sarah Breedlove', 'Dowager Empress Cixi']

print(invited_to_dinner)

invited_to_dinner.remove('Grandma Hart')

print(invited_to_dinner)
invited_to_dinner.insert(0, 'Amelia Earhart')

print(invited_to_dinner)

invited_to_dinner.insert(0, 'Grandma Hart')
invited_to_dinner.insert(4, 'Great Aunt Alice')
invited_to_dinner.append('Hua Mulan')

print(invited_to_dinner)

message = "I'm sorry I can't invite you to dinner "

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

cant_invite = invited_to_dinner.pop()

print(f'{message}{cant_invite}')

message = ", you are formally invited to dinner."

print(f"{invited_to_dinner[0]}{message}")
print(f"{invited_to_dinner[1]}{message}")

## sorting a list/ .sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() 

# cars.sort(reverse = True)

print(cars)

#can also do it this way

print(sorted(cars)) #this makes it temperary

print(cars)
cars.reverse()
print(cars)

print(len(cars))

print('')
print('')
print('')

print('Exercise')
print('')

list_of_locations = ['Elroy', 'Madison', 'Milwakee', 'Appleton', 'Green Bay']

print(list_of_locations)

print(sorted(list_of_locations))

print(sorted(list_of_locations, reverse = True))

print(list_of_locations) #double checking to make sure the original order of the list hasn't changed

list_of_locations.reverse()
print(list_of_locations)

list_of_locations.reverse()
print(list_of_locations)

list_of_locations.sort()
print(list_of_locations)

list_of_locations.sort(reverse = True)
print(list_of_locations)

print(len(invited_to_dinner))

print("")
print("")

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) #IndexError: list index out of range

print(motorcycles[-1]) #Only time this will give you an error will be if the array is empty

