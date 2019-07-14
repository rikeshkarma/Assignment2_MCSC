import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x**2+x
print("x","\t\t","y")
lower=0
upper=2

n=20
h=(upper-lower)/n
x=np.arange(lower,upper,h)
y = np.zeros(len(x))

for i in range(0,len(x)):
    y[i]=y[i-1] + h*f(x[i-1],y[i-1])
    print(round(x[i],5),"\t\t",round(y[i],5))

plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend("Euler")
plt.show()
