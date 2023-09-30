
bicycles=['trek','cannodale','redline','specialized']
print(bicycles)

#Accessing ellements in a list

print(bicycles[0])

print(bicycles[0].title())

#Index positions start at 0, NOT 1

print(bicycles[1])
print(bicycles[2])

#negative indexing

print(bicycles[-1])

# using individual values from a list

message = f"MY first bicycle was a {bicycles[0].title()}."
print(message)

# Modifing, Adding, and Removing elements

#modifing elements in a list

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='dukati'
print(motorcycles)

#addind elements to the list

#appending elements to the end of the list

motorcycles.append('ducati')
print(motorcycles)

#inserting elements into the list

motorcycles.insert(0,'ducati')
print(motorcycles)

#deleting elements in the list
del motorcycles[0]
print(motorcycles)

#removing an item using the pop() method

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

last_owned = motorcycles.pop()
print(f"the last motorcycle i owned was a {last_owned.title()}.")

#poping items from any positon in a list
first_owned = motorcycles.pop(0)
print(f"the first motorcycle i owned was a {first_owned.title()}.")

# removing an item by value
motorcycles.append('ducati')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#The remove() method deletes only the first occurrence of the value you specify.
# If there’s a possibility the value appears more than once in the list, 
# you’ll need to use a loop to make sure all occurrences of the value are removed. 
# You’ll learn how to do this in Chapter 7.

#organizing the list

#sorting a list permanently with the sort() method

cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse= True)
print(cars)

#sorting a list temporarily with the sorted() method

print(sorted(cars))
print(cars)

#Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.
# There are several ways to interpret capital letters when determining a sort order,
# and specifying the exact order can be more complex than we want to deal with at this time. 
# However, most approaches to sorting will build directly on what you learned in this section.

#printing a list in reverse order
cars.reverse()
print(cars)

#finding the length of the list
print(len(cars))

#Python counts the items in a list starting with one, 
# so you shouldn’t run into any off-by-one errors when determining the length of a list.

#avoiding index errors when working with list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

print(motorcycles[-1])



