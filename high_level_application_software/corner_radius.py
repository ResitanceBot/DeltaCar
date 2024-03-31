import numpy as np
from scipy.optimize import curve_fit

def circle(x, a, b, R):
    return np.sqrt(R**2 - (x - a)**2) + b

def curvature(x, a, R):
    return 1 / R

def calculate_radius_of_curvature(points):
    # Ajuste de los puntos a una circunferencia
    x_data = points[:, 0]
    y_data = points[:, 1]

    popt, pcov = curve_fit(circle, x_data, y_data, method='lm')

    # Extracción de los parámetros del círculo ajustado
    a, b, R = popt

    # Cálculo del radio de curvatura
    radius_of_curvature = np.abs(R)

    return radius_of_curvature

# Ejemplo de uso
if __name__ == "__main__":
    # Conjunto de puntos representando una línea
    points = np.array([
        [0, 0],
        [1, 1],
        [2, 4],
        [3, 9],
        [4, 16],
        [5, 25],
        [6, 36]
    ])

    # Calcular el radio de curvatura
    radius = calculate_radius_of_curvature(points)
    print("Radio de curvatura:", radius)