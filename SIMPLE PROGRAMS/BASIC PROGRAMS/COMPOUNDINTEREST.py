# getting three numbers from the user for calculating interest
p = int(input("enter the initial amount: "))
n = int(input("enter the number of years: "))
r = float(input("enter the interest rate: "))



a = p*(1 + r/100)**n

ci = a-p 
print(ci)