import numpy as np
import matplotlib.pyplot as plt
x = ["David", "Mike", "John", "Bob", "Emily", "Tom", "Eve", "Alice", "Sophia", "Sara"]
y = [190, 185, 180, 175, 173, 172, 170, 168, 162, 160]
np.array(x)
np.array(y)
fig, ax = plt.subplots()
plt.title('Student growth')
ax.pie(y, labels = x)
ax.axis("equal")
plt.legend()
plt.show()
