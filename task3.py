n=input("please enter your first name and your family:")
a=float(input("enter your first number:"))
b=float(input("enter your second number:"))
c=float(input("enter your third number:"))
ave=(a+b+c)/3
if ave>=17:
    status="Great"
if ave<17 and ave>=12:
    status="Normal"
if ave<12:
    status="Fall"

print("Dear",n,"your status is",status)   


