import numpy as np
import matplotlib.pyplot as plt

# Define N1D and B1D if not already done
def N1D(xi, nn):
    if nn == 2:
        return [(1 - xi) / 2, (1 + xi) / 2]
    elif nn == 3:
        return [xi * (xi - 1) / 2, 1 - xi**2, xi * (xi + 1) / 2]
    else:
        raise ValueError('Only 2-node or 3-node elements supported')

def B1D(xi, nn):
    if nn == 2:
        return [-0.5, 0.5]
    elif nn == 3:
        return [xi - 0.5, -2 * xi, xi + 0.5]
    else:
        raise ValueError('Only 2-node or 3-node elements supported')

# Generate plotting points
xplot = np.linspace(-1, 1, 100)

# Linear case (2 nodes)
d_linear = np.array([-1, 1])  # nodal values
u_linear = np.zeros_like(xplot)
du_linear = np.zeros_like(xplot)

for i, xi in enumerate(xplot):
    N = N1D(xi, 2)
    B = B1D(xi, 2)
    u_linear[i] = np.dot(N, d_linear)
    du_linear[i] = np.dot(B, d_linear)

# Quadratic case (3 nodes)
d_quad = np.array([1, 0, 1])  # nodal values
u_quad = np.zeros_like(xplot)
du_quad = np.zeros_like(xplot)

for i, xi in enumerate(xplot):
    N = N1D(xi, 3)
    B = B1D(xi, 3)
    u_quad[i] = np.dot(N, d_quad)
    du_quad[i] = np.dot(B, d_quad)

# Plotting
plt.figure(figsize=(10, 6))

# Plot function
plt.subplot(2, 1, 1)
plt.plot(xplot, u_linear, 'r', label='Linear', linewidth=1.5)
plt.plot(xplot, u_quad, 'b', label='Quadratic', linewidth=1.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Function')

# Plot derivative
plt.subplot(2, 1, 2)
plt.plot(xplot, du_linear, 'r', label='Linear', linewidth=1.5)
plt.plot(xplot, du_quad, 'b', label='Quadratic', linewidth=1.5)
plt.legend()
plt.xlabel('x')
plt.ylabel('du/dx')
plt.title('Derivative')

plt.tight_layout()
plt.show()
