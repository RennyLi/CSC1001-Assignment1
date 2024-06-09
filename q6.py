#Import built-in trigonometric functions from the math package
from math import sin
from math import cos
from math import tan

#Prompt the user to enter the interval end points a,b
a=eval(input("Please enter the first interval end point a:"))
b=eval(input("Please enter the second interval end point b:"))

#Avoid the possible errors if the user inputs a floating point number as n
try:
    n=int(input("Please enter the number of sub-intervals n:"))
except:
    print("Your input n is improper!")

#Prompte the user to specify a trigonometric function f
f=input("Please specify a trigonometric function f (f can only be sin,cos or tan):")
#Define the function to func()
def func(f):
    if f=="sin":
        return sin(f)
    elif f=="cos":
        return cos(f)
    else:
        return tan(f)

#The initial sum equals to zero
sum=0
#Calculate the numerical integration
for i in range(1,n+1):
    sum+=(b-a)/n*func(a+(b-a)/n*(i-1/2))

#Display the result
print("The numerical integration of f over",[a,b],"is",sum)