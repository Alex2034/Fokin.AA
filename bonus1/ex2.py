import random
n = 10
a = []
for i in range(n):
    a.append(random.randint(0,100))
print(a)

n = len(a)
for i in range(n):
    t = a[i]
    a[i]=min(a[i:]) # это плохое по эффективности решение. min уже проходится по массиву, а ты тут делаешь это еще раз потом. Можно сделать за 1 проход.
    for j in range(i,n):
        if a[j] == min(a[i:]):
            index = j
    a[index]=t
    print(a)    

print(a)

# 1) нет док-стринга
# 2) не удовлетроряет pep8
# 3) задание было "Напишите функцию, которая...". Функции нет, т.к. весь скпирт целиком - не функция. Функция это def fnc(x1,x2): ...
# оценка 0/10