#CHAPTER 4: WORKING WITH LISTS
#------------------------------


#LOOPING THROUGH AN ENTIRE LIST

magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician)

# Doing more work within a for loop
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")

# Doing something after a for loop
print("Thank you,everyone.That was a great magic show!")


#AVOIDING INDENTATION ERRORS

#forget to indent
magicians = ["alice","david","carolina"]
for magician in magicians:
print(magician)

#forgetting to indent additional lines
magicians = ['alice', 'david', 'carolina']
for magician in magicians:    
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# indenting unnecessarily
message = "hello python"
    print(message)

#indenting unnecessaily after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:    
    print(f"{magician.title()}, that was a great trick!") 
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
   
    print("Thank you everyone, that was a great magic show!")

#forgetting colon

magicians = ['alice', 'david', 'carolina']
for magician in magicians    
    print(f"{magician.title()}, that was a great trick!")    
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#MAKING NEMURICAL LISTS  

#Using the range() function
for value in range(1,5):
    print(value)

#Using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

evennumbers = list(range(2,11,2))
print(evennumbers)

squares = []
for value in range (1,11):
    square = value **2
    squares.append(square)
print(squares)

#Simple statistics with a list of numbers
digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))

#The examples in this section use short lists of numbers that fit easily on the page. 
# They would work just as well if your list contained a million or more numbers.

#LIST COMPREHENSIONS

squares=[value**2 for value in range (1,11)]
print(squares)

#WORKING WITH PART OF A LIST

#Slicing a list
players = ["charles","martina","michael","florence","eli"]
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

#You can include a third value in the brackets indicating a slice. 
# If a third value is included, 
# this tells Python how many items to skip between items in the specified range.

#LOOPING THROUGH A SLICE

print("Here are the first three players on my team:")
for player in players[:3]:    
    print(player.title())

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#Don’t worry about the details in this example for now. 
# If you’re trying to work with a copy of a list and you see unexpected behavior, 
# make sure you are copying the list using a slice, as we did in the first example.


#TUPLES

dimentions = (200,50)
print(dimentions[0])
print(dimentions[1])

#Tuples are technically defined by the presence of a comma; 
# the parentheses make them look neater and more readable. 
# If you want to define a tuple with one element, 
# you need to include a trailing comma:

#    my_t = (3,)

#It doesn’t often make sense to build a tuple with one element, 
# but this can happen when tuples are generated automatically.

#Looping through all values in a tuple

for dimention in dimentions:
    print(dimention)

#Writing over a tuple
dimentions = (200,50)
print("Original dimentions:")
for dimention in dimentions:    
    print(dimention)
    dimentions = (400, 100)
    print("\nModified dimensions:")
for dimention in dimentions:   
    print(dimention)

#STYLING YOUR CODE
#   -indentation
#   -line length
#   -blank lines
