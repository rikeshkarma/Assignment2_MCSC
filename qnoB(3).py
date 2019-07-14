# Implement Trapezoidal-rule to approximate the definite integral 𝐼 = 𝑠𝑖𝑛𝑥 𝑒𝑥
#𝑑𝑥
#𝜋 0 by taking 20-equal
#divisions of the interval [0,𝜋]. (Algorithm: 𝑰 = 𝒉 𝟐

import numpy as np
import math as m

print("x"+"\t\t"+"  y")
def f(x):
    return (m.sin(x))/(m.exp(x))

lower=0
upper=180
trap=0

n=20
h=(upper-lower)/n
x=np.arange(lower,upper,h)
y=[]

for i in range(len(x)):
    y.append(f(x[i]))
    print(x[i],"\t\t",y[i])

trap=y[0]+y[-1]
for i in range(1,len(x)-1):
    trap +=2*y[i]

trap=h/2*trap
print("\nTrapezoidal rule: "+ str(trap))
