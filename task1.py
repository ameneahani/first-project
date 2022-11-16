import math
a=float(input("enter first number:"))
print("+","-","/","*")
print("sin","cos","tan","cot")
print("factorial","sqrt")
op=input("choose your operation:")
if op=="+" or op=="-" or op=="*" or op=="/":
    b=float(input("enter second number:"))
    if op=="+":
        c=a+b
    elif op=="-":
        c=a-b
    elif op=="/":
        if b==0:
            c="infinity"
        else:
            c=a/b
    elif op=="*":
        c=a*b
elif op=="sin": 
    a=a*math.pi/180
    c=math.sin(a)
elif op=="cos":
    a=a*math.pi/180
    c=math.cos(a)
elif op=="tan":
    if a==90 or a==270:
        c="infinity"
    else: 
        a=a*math.pi/180
        c=math.tan(a)
elif op=="cot":
    if a==0 or a==180 or a==360:
        c="infinity"
    else:
        a=a*math.pi/180
        c=1/math.tan(a)
elif op=="factorial":
    a=int(a)
    c=math.factorial(a)
elif op=="sqrt":
    c=math.sqrt(a)


print(c)       
