import math
n=20
a=[]
x0=100
y0=100
a=50
b=10
for k in range (n):
    a.append((x0+a*math.cos(k*2*math.pi/n),y0+b*math.sin(k*2*math.pi/n)))

print(a)

