# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = [100, 100, 3, 5, 6, 7, 3, 3]
lst = [el for el in lst if lst.count(el) == 1]
print(lst)
