
print("HELLO WORLD PYTHON!")


# VARIABLES
#-----------

message = "HELLO WORLD PYTHON!"
print(message)

message = "HELLO  PYTHON CRASH COURSE WORLD!"
print(message)

# Naming Using Variables

#The Python variables you’re using at this point should be lowercase. 
# You won’t get errors if you use uppercase letters, 
# but uppercase letters in variable names have spe-cial meanings that we’ll discuss in later chapters.

#Avoiding Name Errors When Using Variables

message = "Hello Crash Course Reader!"
print(mesage)

#NameError: name 'mesage' is not defined. Did you mean: 'message'?


mesage = "Hello Crash Course Reader!"
print(mesage)

#Variables Are Labels

#The best way to understand new programming concepts is to try using them in your programs. 
# If you get stuck while working on an exercise in this book, try doing some-thing else for a while. 
# If you’re still stuck, review the relevant part of that chapter. 
# If you still need help, see the suggestions in Appendix C.


#STRINGS
#-------

"This is a string"
'This is also a string'
'I told my friend,"python is my favourite language!"'
"one of python's strangths is its diversity and supportive community"

#Changing Case in a String with Methods

name = "ada lovelace"
print(name.title()) 
#title() capatilize the each character's first letter

print(name.upper)
print(name.lower)


#Using Variables in Strings

first_name = "ada"
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
#string formatting
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f'Hello, {full_name.title()}!'
print(message)

# Adding Whitespace to Strings with Tabs or Newlines

print("python")
print('\tpython')
# adds a tab space
print("Lamguages:\npython\nc\njava")
# adds in a new line
print("Lamguages:\n\tpython\n\tc\n\tjava")
# add new line with tab space


#Stripping Whitespace

favourite_language ="python world"
print(favourite_language)
favourite_language = favourite_language.strip()
print(favourite_language)

#Removing Prefixes

nostarch_url= "https://nostarch.com"
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)

#Avoiding Syntax Errors with strings"apostrophe"

message = "one of python's strengths is its diverse community"
print(message)

message = 'one of python's strengths is its diverse community'
print(message)

#Your editor’s syntax highlighting feature should help you spot some syntax errors quickly as you write your programs.
# If you see Python code highlighted as if it’s English or English highlighted as if it’s Python code, 
# you probably have a mismatched quotation mark somewhere in your file.

#NUMBERS
#-------


#integers
print(2+3)
print(2-3)
print(2*3)
print(3/2)
print(3//2)
print(3%2)
print(3**2)
print(2+3*4)
print((2+3)*4)

#float
print(0.1+0.1)
print(0.2-0.1)
print(2*0.1)
print(3*0.1)

#integers and floats

print(4/2)
print(1+3.0+2.9)
print(3.0**5)

#under scores in numbers

universe_age=14_000_000_000
print(universe_age)

#multiple assignment

x,y,z = 1,2,3
print(x,y,z)

#constants

MAX_CONNECTIONS = 5000

#comments

#say hello to everyone.
print("hello python people!")


# The Zen of python

import this




