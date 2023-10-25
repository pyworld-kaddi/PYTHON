# getting a number from user for finding factorial of that number
n = int(input("enter the number for factorial"))
sum = 1
# ignoring 1 and 0 because their factorial is 1 only
if n == 0 or n == 1:
    print(1)
else:
# finding factorial of the given number
    for i in range(n,0,-1):
        sum *= i
print (sum)
        