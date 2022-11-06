
s = ['1', '2', '3', '4', '5']

#Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.

for i in s:
    i = int(i)
x_min = min(s)
x_max = max(s)
print(x_min, x_max)
x_min_ind = s.index(x_min)
x_max_ind = s.index(x_max)
print(x_min_ind, x_max_ind)
s[x_min_ind] = x_max
s[x_max_ind] = x_min
print(s)