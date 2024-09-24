import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de las ecuaciones
A = np.array([[1, 1.0001],
              [1, 1]])
b = np.array([2, 2])

# Resolver el sistema de ecuaciones lineales
sol = np.linalg.solve(A, b)
x1_sol, x2_sol = sol

# Crear valores de x2 para graficar las líneas
x2_vals = np.linspace(0, 4, 400)

# Ecuaciones de las líneas
x1_eq1 = 2 - 1.0001 * x2_vals  # De la ecuación x1 + 1.0001x2 = 2
x1_eq2 = 2 - x2_vals           # De la ecuación x1 + x2 = 2

# Graficar
plt.plot(x2_vals, x1_eq1, label=r'$x_1 + 1.0001x_2 = 2$')
plt.plot(x2_vals, x1_eq2, label=r'$x_1 + x_2 = 2$')

# Marcar la solución en la gráfica
plt.scatter(x2_sol, x1_sol, color='red', zorder=5)
plt.text(x2_sol, x1_sol, f'({x1_sol:.4f}, {x2_sol:.4f})', fontsize=12, ha='right')

# Configuraciones de la gráfica
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim([0, 3])
plt.ylim([0, 3])
plt.xlabel(r'$x_2$')
plt.ylabel(r'$x_1$')
plt.legend()
plt.title('Gráfico de las ecuaciones')
plt.grid(True)
plt.show()
