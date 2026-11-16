n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = []
for i in range(n):
    row = [int(x) for x in input(f"Введите элементы строки {i + 1} через пробел: ").split()]
    matrix.append(row)

print("Матрица:")
for row in matrix:
    print(*row)

sums = [sum(row) for row in matrix]
max_sum = max(sums)

print("Суммы элементов строк:", sums)
print("Максимальная сумма элементов:", max_sum)

for i in range(n):
    if sums[i] == max_sum:
        print(f"Строка с максимальной суммой: номер {i + 1}, элементы {matrix[i]}")
        