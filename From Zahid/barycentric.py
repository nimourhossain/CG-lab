import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Ray
o = np.array([1, 1, 1])
d = np.array([-1, -1, -1])

# Triangle vertices
v0 = np.array([1, 0, 0])
v1 = np.array([0, 1, 0])
v2 = np.array([0, 0, 1])

# Edges
e1 = v1 - v0
e2 = v2 - v0

# Möller–Trumbore intersection
h = np.cross(d, e2)
a = np.dot(e1, h)
if abs(a) < 1e-6:
    print("Ray is parallel to triangle")
else:
    f = 1 / a
    s = o - v0
    u = f * np.dot(s, h)
    q = np.cross(s, e1)
    v = f * np.dot(d, q)
    t = f * np.dot(e2, q)

    if 0 <= u <= 1 and 0 <= v <= 1 and u + v <= 1:
        p = o + t * d  # intersection point
        print(f"Ray hits the triangle at t = {t:.2f}")
        print(f"Barycentric coordinates: (u, v, w) = ({u:.2f}, {v:.2f}, {1 - u - v:.2f})")
        
        # Plotting
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Triangle
        tri = [v0, v1, v2]
        ax.add_collection3d(Poly3DCollection([tri], color='cyan', alpha=0.5))

        # Ray line
        t_vals = np.linspace(0, t + 1, 10)
        ray = o[:, None] + d[:, None] * t_vals
        ax.plot(ray[0], ray[1], ray[2], color='red', label='Ray')

        # Intersection point
        ax.scatter(*p, color='green', s=50, label='Intersection')

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.legend()
        plt.show()
    else:
        print("No intersection inside the triangle")
