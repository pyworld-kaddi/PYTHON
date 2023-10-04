#CHAPTER 5: IF STATEMENTS
#-------------------------


#A simple examle
cars = ["audi", "bmw", "subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
    
#conditional tests

#checking for equality
car = "bmw"
print(car == "bmw")
      
#ignoring case when checking for equality
print (car == "BMW")
    

#checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#numerical comparisons
age= 18
print(age == 18)

answer = 17
if answer != 42:    
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21) 

#checking multiple conditions (and)
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

#checking multiple conditions (or)
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

#checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

#checking whether a value is notin a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:    
    print(f"{user.title()}, you can post a response if you wish.")

#BOOLEAN EXPRESSIONS
Game_active = True
can_edit = False

#IF STATEMENTS

#simple if statements
if conditional_test:
    do something

age = 19
if age >= 18:
    print("you are old enough to vote!")

#if-else statements

age = 17
if age >= 18:
    print("you are old enough to vote!")
else:
    print("sorry you are too young to vote!")

#if-elif-else statements

age = 12
if age < 4:    
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:    
    price = 25
elif age < 65:    
    price = 40
else:    
    price = 20
print(f"Your admission cost is ${price}.")

#omiting the else block
age = 12
if age < 4: 
    price = 0
elif age < 18:    
    price = 25
elif age < 65:    
    price = 40
elif age >= 65:   
    price = 20
print(f"Your admission cost is ${price}.")

#testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:    
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:    
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:    
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#USING IF STATEMENT WITH THE LISTS

#checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:    
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#checking that list is not empty
requested_toppings = []
if requested_toppings:    
    for requested_topping in requested_toppings:        
        print(f"Adding {requested_topping}.")    
    print("\nFinished making your pizza!")
else:    
    print("Are you sure you want a plain pizza?")

#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
    
print("\nFinished making your pizza!")

#styling your if statements

if age < 4:
#is better than:
if age<4:

