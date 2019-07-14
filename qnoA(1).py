#1. Implement the Bisection Method to approximate the root of the equation
#𝑥2 = 𝑠𝑖𝑛𝑥 by taking the initial guesses 𝑎 = 0.5 𝑎𝑛𝑑 𝑏 = 1.0.

import math as m

a=0.5
b=1.0
n=0
print("Iteration"+"\ta"+"\tb"+"\tc=(a+b)/2"+"\tf(a)"+"\tf(b)"+"\tf(c)")

while n<=10:
    c=((a+b)/2)
    fa=a**2-m.sin(a)
    fb=b**2-m.sin(b)
    fc=c**2-m.sin(c)
    if fc<0:
        a=c
        b=b
        n=n+1
        print(str(n)+"\t\t"+str(round(a,3))+"\t"+str(round(b,3))+"\t"+str(round(c,3))+"\t\t"+str(round(fa,3))+"\t"+str(round(fb,3))+"\t"+str(round(fc,3)))

    else:
        b=c
        a=a
        n=n+1
        print(str(n)+"\t\t"+str(round(a,3))+"\t"+str(round(b,3))+"\t"+str(round(c,3))+"\t\t"+str(round(fa,3))+"\t"+str(round(fb,3))+"\t"+str(round(fc,3)))

print("The approximate root of the equation is: "+str(round(c,3)))
