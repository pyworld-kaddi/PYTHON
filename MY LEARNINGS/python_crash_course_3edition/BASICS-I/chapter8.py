#CHAPTER 8: Functions
#---------------------

# defining function
def greet_user(): # type: ignore
    """DISPLAY a simple greeting"""
    print("Hello!")
greet_user()

#Passing information to a funtion

def greet_user(name):
    """ DISPLAY a simple greeting"""
    print(f"Hello, {name.title()}")
greet_user("Jesse")

#Arguments and parameters

#People sometimes speak of arguments and parameters interchangeably. 
#Don’t be sur-prised if you see the variables in a function definition referred to as arguments or
#the variables in a function call referred to as parameters.

#Passing Arguments

#positional arguments
def describe_pet (animal_type, pet_name):    # type: ignore
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")    
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

#multiple Function cells
def describe_pet(animal_type, pet_name):    # type: ignore
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")    
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog','willie')

#Order matters in positional arguments
def describe_pet(animal_type, pet_name):   # type: ignore 
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")    
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry','hamster')

#keyword arguments
def describe_pet(animal_type, pet_name):    # type: ignore
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")    
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='harry',pet_name='hamster')

#When you use keyword arguments, be sure to use the exact 
#names of the parameters in the function’s definition.

#Default values
def describe_pet(pet_name, animal_type='dog'):   # type: ignore
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")    
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

#When you use default values,any parameter with a default value needs 
#to be listed after all the parameters that don’t have default values. 
#This allows Python to con-tinue interpreting positional arguments correctly

#Equivalent Function calls
def describe_pet(pet_name, animal_type='dog'):# type: ignore
    
    
#Avoid Arguments Errors
def describe_pet(pet_name, animal_type='dog'):   # type: ignore
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")    
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()

#return values
#returning a simple value
def get_formatted_name(first_name, last_name):   #type:ignore 
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name(first_name, middle_name, last_name):    #type:ignore
	"""Return a full name, neatly formatted."""    
	full_name = f"{first_name} {middle_name} {last_name}"    
	return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''): #type: ignore
	"""Return a full name, neatly formatted."""
	if middle_name:        
		full_name = f"{first_name} {middle_name} {last_name}"
	else:        
		full_name = f"{first_name} {last_name}"    
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#returning a dictionary
def build_person(first_name, last_name):    #type:ignore
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person."""    
	person = {'first': first_name, 'last': last_name}    
	if age:        
		person['age'] = age    
	return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Using a function with a while loop
def get_formatted_name(first_name, last_name):    #type: ignore
	"""Return a full name, neatly formatted."""    
	full_name = f"{first_name} {last_name}"    
	return full_name.title()
# This is an infinite loop!
a=2
while a==1:#while True
		print("\nPlease tell me your name:")    
        f_name = input("First name: ")    #type: ignore
        l_name = input("Last name: ")    #type: ignore
        formatted_name = get_formatted_name(f_name, l_name)    
        print(f"\nHello, {formatted_name}!")
    

#passing a list
def greet_users(names):   #type:ignore 
	"""Print a simple greeting to each user in the list."""    
	for name in names:        
		msg = f"Hello, {name.title()}!"        
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#modifying a list in a function
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:    
	current_design = unprinted_designs.pop()   
	print(f"Printing model: {current_design}")    
	completed_models.append(current_design)
	# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:    
	print(completed_model)

#Preventing a function from MOdifying a list
function_name(list_name[:]) #type:ignore 
print_models(unprinted_designs[:], completed_models) #type:ignore

#passing an arbitary number of arguments
def make_pizza(*toppings):    #type:ignore
	"""Print the list of toppings that have been requested."""    
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#mixing POsitional and Arbitary arguments
def make_pizza(size, *toppings):    #type: ignore
	"""Summarize the pizza we are about to make."""    
	print(f"\nMaking a {size}-inch pizza with the following toppings:")    
	for topping in toppings:        
		print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#You’ll often see the generic parameter name *args, 
# which collects arbitrary positional arguments like this.

#Using arbitrary keywords Arguments
def build_profile(first, last, **user_info):    #type:ignore
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first    
	user_info['last_name'] = last    
	return user_info
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

#You’ll often see the parameter name  **kwargs 
# used to collect nonspecific keyword arguments.

#Storing your functions in modules

#importig an entire module
def make_pizza(size, *toppings):    #type:ignore
    """Summarize the pizza we are about to make."""   
    print(f"\nMaking a {size}-inch pizza with the following toppings:")    
    for topping in toppings:        
        print(f"- {topping}")
#Now we’ll make a separate file called making_pizzas.py 
# in the same directory as pizza.py.

import pizza #type : ignore
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#importing specific functions
from module_name import function_name
from module_name import function_0, function_1, function_2
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to give a function alias
from pizza import make_pizza as mp
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to give a module an alias
import pizza as p
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#importing all functions in a module
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

from module_name import *

#Styling functions
def dunction_name(parameter_0, parameter_1='default value')

function_name(value_0,parameter_1='value')

def function_name(parameter_0,parameter_1,parameter_2,parameter_3,parameter_4,parameter_5):
    function body ....
