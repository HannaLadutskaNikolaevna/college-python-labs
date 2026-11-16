
input_str = input("Введите элементы массива через пробел: ")
arr = [int(x) for x in input_str.split()]

print("Исходный массив:", arr)
print("Массив после реверса (алгоритмический):", arr)
arr = arr[::-1]
