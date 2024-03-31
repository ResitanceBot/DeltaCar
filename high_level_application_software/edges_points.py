import cv2
import numpy as np

class EdgeExtractor:
    def __init__(self):
        pass

    def extract_edges(self, binarized_image):
        # Encuentra los contornos en la imagen binarizada
        contours, _ = cv2.findContours(binarized_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Crea una lista para almacenar los bordes
        edges = []

        # Recorre cada contorno y extrae los puntos del borde
        for contour in contours:
            edge_points = []
            for point in contour:
                x, y = point[0]
                edge_points.append((x, y))
            edges.append(edge_points)

        return edges

# Ejemplo de uso
if __name__ == "__main__":
    # Carga la imagen binarizada
    binarized_image = cv2.imread("binarized_image.png", cv2.IMREAD_GRAYSCALE)

    # Crea una instancia del extractor de bordes
    edge_extractor = EdgeExtractor()

    # Extrae los bordes de la imagen
    edges = edge_extractor.extract_edges(binarized_image)

    # Imprime los puntos de cada borde
    print("Conjunto de listas con los puntos de los bordes:")
    for i, edge in enumerate(edges):
        print(f"Borde {i+1}: {edge}")
