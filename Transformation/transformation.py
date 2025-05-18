import numpy as np
import matplotlib.pyplot as plt

def transform_and_plot(ax, matrix, title):
    transformed = matrix @ shape
    ax.plot(shape[0], shape[1], 'bo-', label='Original')
    ax.plot(transformed[0], transformed[1], 'r--', label='Transformed')
    ax.set_title(title)
    ax.legend()
    ax.grid()

shape = np.array([[0, 1, 1, 0, 0],
                  [0, 0, 1, 1, 0],
                  [1, 1, 1, 1, 1]])

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

transform_and_plot(axs[0, 0], np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]]), "Scaling")
transform_and_plot(axs[0, 1], np.array([[1, 1.2, 0], [0, 1, 0], [0, 0, 1]]), "Shearing")
transform_and_plot(axs[1, 0], np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]), "Rotation")
transform_and_plot(axs[1, 1], np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]]), "Reflection")

plt.tight_layout()
plt.show()
