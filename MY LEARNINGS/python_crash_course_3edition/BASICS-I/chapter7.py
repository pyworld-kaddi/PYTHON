#CHAPTER 7: USER INPUT AND WHILE LOOPS
#--------------------------------------

#How the input() function works
message = input("tell me something, and I will repeat it back to you: ")
print(message)

#Some text editors won’t run programs that prompt the user for input. 
#You can use these editors to write programs that prompt for input, 
#but you’ll need to run these programs from a terminal. 
#See “Running Python Programs from a Terminal” on page 11.

#Writing clear prompts
name = input ("please enter your name: ")
print(f"\nhello,  {name}!")

prompt = "if you share your name, we can personalize the mesages you see."
prompt += "\n What is your name? "
name = input(prompt)
print(f"\nhello, {name}!")

#using int() to accept numerical inputs

age = input("how old are you? ")
print(age)
print(type(age))

age= int(age)
print(age)
print(type(age))

#modulo operator
# even or odd numbers
number = int(input("enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
    
#Introducing While loops
#the while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':    
    message = input(prompt)    
    print(message)
    
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':    
    message = input(prompt)    
    
    if message != 'quit':
        print(message)
        
#Using flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:    
    message = input(prompt)    
    if message == 'quit':        
        active = False    
    else:        
        print(message)
        
#Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:    
    city = input(prompt)    
    if city == 'quit':        
        break    
    else:        
        print(f"I'd love to go to {city.title()}!")
        
#You can use the break statement in any of Python’s loops. 
# For example, you could use break to quit a for loop that’s working 
# through a list or a dictionary.

#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1    
    if current_number % 2 == 0:        
        continue    
    print(current_number)

#Avoiding infinite loops
x = 1
while x <= 5:    
    print(x)    
    x += 1

#VS Code, like many editors, displays output in an embedded terminal window. 
# To cancel an infinite loop,make sure you click in the output area of the 
# editor before pressing CTRL-C.

#Using a while loop with lists and dictionaries
#Moving items from one list to another

#Start with users that need to be verified,
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    # Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:    
        print(confirmed_user.title())
        
#Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:    
    pets.remove('cat')
print(pets)

# Filling a dictionary with user input
responses = {}
# Set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


    
    