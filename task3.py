# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


n = list(input('Введите число: '))

list = n
print(list)

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print(result)