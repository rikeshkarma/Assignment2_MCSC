import numpy as np
import math as m

print("x"+"\t\t"+"  y")
def f(x):
    return (m.sqrt(1/(2*180)))*m.exp(-(x*x/2))

lower=-4
higher=4

n=50
h=(higher-lower)/n
x=np.arange(lower,higher,h)
y=[]

for i in range(len(x)):
    y.append(f(x[i]))
    print(round(x[i],7),"\t\t",round(y[i],7))

sim=y[0]+y[-1]
sim=sim+4*sum(y[1:-1:2])+2*sum(y[2:len(y)-1:2])
sim=(h/3)*sim

print("The Simpson 1/3-rule: "+str(sim))
