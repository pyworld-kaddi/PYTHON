# getting three numbers from the user for calculating interest
p = int(input("enter the initial amount: "))
n = int(input("enter the number of years: "))
r = float(input("enter the interest rate: "))

# calculating interest
i = (p*n*r)/100

print("Simple interest for the given information is", i)
