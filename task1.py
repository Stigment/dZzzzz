# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  


import math
x = math.pi
n = input('Введите число d: ')
count = 0

n = n.replace('0.', '')

for i in n:
    count+=1

print(f'Число {x:.{count}f}')