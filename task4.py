w=float(input("please enter your weight(Kg):"))
h=float(input("please enter your height(m):"))
BMI=w/(h*h)
if BMI<18.5:
    status="UNDERWEIGHT"
elif BMI>=18.5 and BMI<25:
    status="NORMAL"
elif BMI>=25 and BMI<30:
    status="OVERWEGHT"
elif BMI>=30 and BMI<35:
    status="OBESE"
elif BMI>=35:
    status="/exTREMLY OBESE"

print("your fitness status is",status)
