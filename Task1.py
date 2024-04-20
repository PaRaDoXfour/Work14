import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def Y(x):
    return 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Значення x в інтервалі [0, 5]
x = np.linspace(0.01, 5, 400)  # Використовуємо 0.01 замість 0, щоб уникнути ділення на нуль

# Значення функції Y(x)
y = Y(x)

# Побудова графіка
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$Y(x) = \frac{5 \cdot \cos(10x) \cdot \sin(3x)}{\sqrt{x}}$')

# Додавання осей
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Позначення осей
plt.xlabel('x')
plt.ylabel('Y(x)')

# Назва графіка
plt.title('Графік функції Y(x)')

# Встановлення меж для відображення
plt.xlim(0, 5)
plt.ylim(-8, 8)

# Виведення легенди
plt.legend()

# Відображення графіка
plt.grid(True)
plt.show()
