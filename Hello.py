import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Создание графика
plt.plot(x, y)

# Добавление заголовков
plt.title("Пример графика")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Вывод графика
plt.show()
