# getting three different numbers from user for finding minimum and maximum among them
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

#printing whicht MAXIMUM among them
if a > b and a > c:
    print("first value is greater, that is",a)
elif b > c:
    print("second value is greater, that is",b)
else:
    print("third value is greater, that is",c)
    
#printing whicht MINIMUM among them
if a < b and a < c:
    print("first value is smaller, that is",a)
elif b < c:
    print("second value is smaller, that is",b)
else:
    print("third value is smaller, that is",c)