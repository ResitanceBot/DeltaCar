import cv2
import numpy as np

def filter_and_enhance(image_path):
    # Leer la imagen
    original_image = cv2.imread(image_path)
    
    # Convertir la imagen a espacio de color HSV
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    
    # Definir los límites del color para el trazado grueso de la trayectoria en HSV
    lower_bound = np.array([166, 100, 37])
    upper_bound = np.array([179, 255, 255])
    
    # Filtrar la imagen para resaltar los trazados gruesos de la trayectoria
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    
    # Aplicar el filtro morfológico para mejorar la forma de los trazados
    kernel = np.ones((7,7),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Aplicar la operación de erosión para adelgazar la línea
    eroded_mask = cv2.erode(mask, kernel, iterations=1)
    
    # Se aplica binarizacion de la mascara para obtener la imagen resultante
    result_image = np.ones_like(original_image) * 255
    result_image[eroded_mask == 0] = 0
    result_image=cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)

    result_image= cv2.ximgproc.thinning(result_image)

    # Crear una copia de la imagen original para mostrar las partes blancas de la imagen mejorada
    overlay_image = original_image.copy()
    
    # Reemplazar los píxeles de la copia con los píxeles blancos de la imagen mejorada
    overlay_image[result_image == 255] = [255, 255, 255]
    
    # Redimensionar las imágenes para que se ajusten a la pantalla
    height, width = original_image.shape[:2]
    scale_factor = 0.5
    scaled_original = cv2.resize(original_image, (int(width*scale_factor), int(height*scale_factor)))
    scaled_result = cv2.resize(overlay_image, (int(width*scale_factor), int(height*scale_factor)))
    
    # Mostrar la imagen original y la imagen resultante
    cv2.imshow('Enhanced Image', scaled_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ruta de la imagen
image_path = 'foto1.jpg'

# Llamar a la función para filtrar y mejorar la imagen
filter_and_enhance(image_path)
