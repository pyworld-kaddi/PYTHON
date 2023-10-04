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
favorite_languages = {'jen':'python','sarah':'c','edward':'rust','phil':'python','}

#Most editors have some functionality that helps you format extended lists and dic-tionaries in a similar manner to this example. 
#Other acceptable ways to format long dictionaries are available as well, so you may see slightly different formatting in your editor, 
#or in other sources.

#Using get() to Access values
pg--97
