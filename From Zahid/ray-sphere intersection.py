import numpy as np
import matplotlib.pyplot as plt

# Ray: R(t) = (1,1,1) + t*(-1,-1,-1)
o = np.array([1, 1, 1])   # origin
d = np.array([-1, -1, -1])  # direction
d = d / np.linalg.norm(d)   # normalize

# Sphere: x^2 + y^2 + z^2 = 1
# Solve ||o + td||^2 = 1 --> quadratic in t: At^2 + Bt + C = 0
A = np.dot(d, d)
B = 2 * np.dot(o, d)
C = np.dot(o, o) - 1

# Solve quadratic
discriminant = B**2 - 4*A*C
t1 = (-B - np.sqrt(discriminant)) / (2*A)
t2 = (-B + np.sqrt(discriminant)) / (2*A)

# Intersection points
p1 = o + t1*d
p2 = o + t2*d

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Sphere
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_surface(x, y, z, alpha=0.2, color='blue')

# Ray line
t_vals = np.linspace(-1, 2, 100)
ray = o[:, None] + d[:, None] * t_vals
ax.plot(ray[0], ray[1], ray[2], color='red', label='Ray')

# Points
ax.scatter(*p1, color='green', s=50, label='Intersection 1')
ax.scatter(*p2, color='purple', s=50, label='Intersection 2')

ax.legend()
plt.show()

print("Ray parameters (t):", t1, t2)
