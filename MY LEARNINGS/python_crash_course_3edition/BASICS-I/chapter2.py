
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

#Avoiding Syntax Errors with strings
