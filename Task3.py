import numpy as np
import matplotlib.pyplot as plt

# Створюємо списки з іменами студентів та їхнім зростом
x = ["David", "Mike", "John", "Bob", "Emily", "Tom", "Eve", "Alice", "Sophia", "Sara"]
y = [190, 185, 180, 175, 173, 172, 170, 168, 162, 160]

# Хоча тут створюються NumPy масиви, вони не використовуються в подальшому коді.
np.array(x)
np.array(y)

# Створення об'єкта графіку
fig, ax = plt.subplots()

# Надаємо назву графіку
plt.title('Student Growth')

# Створюємо кругову діаграму
ax.pie(y, labels=x)

# Встановлюємо, щоб осі були однаково масштабовані, тобто круг має бути кругом, а не еліпсом
ax.axis("equal")

# Вивід легенди, що допомагає ідентифікувати, який сектор відповідає якому студенту
plt.legend()

# Показуємо графік
plt.show()
