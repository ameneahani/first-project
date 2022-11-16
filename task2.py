a=float(input("enter the first side of the triangle:"))
b=float(input("enter the second side of the triangle:"))
c=float(input("enter the third side of the triangle:"))
if a<(b+c):
    if b<(a+c):
        if c<(a+b):
            print("yes")
else:
    print("no")