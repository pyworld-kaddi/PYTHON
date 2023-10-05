#CHAPTER 6: DICTIONARIES
#------------------------

# A simple dictionary
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#working with dictionaries

#accessing values in a dictionary
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])

#adding new key-value pairs to the dictionary
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#starting with a empty dictionary
alien_0 = {}
print(alien_0)
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#modifying values in a dictionary
alien_0['color']='yellow'
print(alien_0)

#removing key-value pairs
del alien_0['points']
print(alien_0)

#Be aware that the deleted key-value pair is removed permanently.

#A dictionary of similar objects
favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}

#Most editors have some functionality that helps you format extended lists 
#and dic-tionaries in a similar manner to this example.Other acceptable ways 
#to format long dictionaries are available as well, so you may see slightly 
# different formatting in your editor, or in other sources.

#Using get() to Access values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#if you leave out the second argument in the call to get() and the key doesn’t exist,
# Python will return the value None. The special value None means “no value exists.” 
# This is not an error: it’s a special value meant to indicate the absence of a value. 
# You’ll see more uses for None in Chapter 8.

#LOOPING THROUGH a dictionary
user_0 = {'username': 'efermi','first': 'enrico','last': 'fermi'}
for key, value in user_0.items():
    print(f"\nkey:{key}")
    print(f"value:{value}")

favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for name, language in favorite_languages.items():    
    print(f"{name.title()}'s favorite language is {language.title()}.")
 
#looping through all the keys in the dictionary
favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for name in favorite_languages.keys():    
    print(name.title())
    
#looping through dictionary's keys in a particular order
favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for name in sorted( favorite_languages.keys()):    
    print(f"{name.title()},thank you for taking the poll.")

#looping through all values in the dictionary
favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for language in favorite_languages.values():    
    print(language.title())

#You can build a set directly using braces and separating the elements with commas:
#  
#       >>> languages = {'python', 'rust', 'python', 'c'}
#       >>> languages
#       {'rust', 'python', 'c'}

#It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
#When you see braces but no key-value pairs, you’re probably looking at a set. 
#Unlike lists and dictionaries, sets do not retain items in any specific order.

#nesting

#A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:    
    print(alien)
    
#A list in dictionary
#Store information about a pizza being ordered.
pizza = {'crust': 'thick','toppings': ['mushrooms', 'extra cheese']}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")
for topping in pizza['toppings']:    
    print(f"\t{topping}")
    
#You should not nest lists and dictionaries too deeply. If you’re nesting items much
#deeper than what you see in the preceding examples,or if you’re working with someone
#else’s code with significant levels of nesting, there’s most likely a simpler way to 
#solve the problem.

# A Dictionary in a dictionary
users = {'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton'},'mcurie': {'first': 'marie','last': 'curie','location': 'paris'},}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"    
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")    
    print(f"\tLocation: {location.title()}")
    



