import numpy as np
import matplotlib.pyplot as plt
print("Population of children 7-11 ages in Albania for 15 years: ")
x = ["David", "Mike", "John", "Bob", "Emily", "Tom", "Eve", "Alice", "Sophia", "Sara"]
y = [190, 185, 180, 175, 173, 172, 170, 168, 162, 160]
np.array(x)
np.array(y)
fig, ax = plt.subplots()
ax.pie(y, labels = x)
ax.axis("equal")
plt.legend()
plt.show()