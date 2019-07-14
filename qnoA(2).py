#Implement the Newton-Raphson’s Method to approximate the root of the equation
#𝑒𝑥 = 4𝑥 by taking the initial guess 𝑥0 = 1.0

import math as m

print("Iteration"+"\t"+"xn"+"\t"+"xn+1"+"\t"+"f(xn+1)")
x=1.0
n=0

while n<=4:
    y=x-((m.exp(x)-4*x)/(m.exp(x)-4))
    print(str(n+1)+"\t\t"+str(round(x,5))+"\t"+str(round(y,5))+"\t"+str(round((m.exp(x)-4*x),5)))
    x=y
    n=n+1
print("The approximate root of the equation is: "+str(round(x,5)))
