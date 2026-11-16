firms = ("Диалог", "Avicom", "Нэта", "Сервер", "Декада", "Dega.ru")

print("Компьютерные фирмы:")
for i in range(len(firms)):
    print(f"{i + 1} - {firms[i]}")

n = int(input("Введите количество вузов: "))

purchases = []
for i in range(n):
    numbers = input(f"Введите номера фирм, в которых закупал вуз {i + 1} (через пробел): ")
    bought = set()
    for x in numbers.split():
        bought.add(firms[int(x) - 1])
    purchases.append(bought)

result = set()
for bought in purchases:
    result = result | bought

print("Закупки по вузам:")
for i in range(n):
    print(f"Вуз {i + 1}:", ", ".join([f for f in firms if f in purchases[i]]))

print("Фирмы, в которых закупка производилась хотя бы одним из вузов:")
print(", ".join([f for f in firms if f in result]))
