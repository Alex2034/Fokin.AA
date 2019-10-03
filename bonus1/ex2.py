import random
n = 10
a = []
for i in range(n):
    a.append(random.randint(0,100))
print(a)

n = len(a)
for i in range(n):
    t = a[i]
    a[i]=min(a[i:])
    for j in range(i,n):
        if a[j] == min(a[i:]):
            index = j
    a[index]=t
    print(a)    

print(a)
