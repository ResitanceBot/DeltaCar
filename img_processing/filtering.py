import cv2
import numpy as np
import time
import skimage.morphology as morph


def filter_and_enhance(image_path):
    # Leer la imagen
    start_time = time.time()
    original_image = cv2.imread(image_path)
    print("Tiempo de procesamiento para leer la imagen:", time.time() - start_time, "segundos")
    
    # Convertir la imagen a espacio de color HSV
    start_time = time.time()
    hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
    print("Tiempo de procesamiento para convertir la imagen a HSV:", time.time() - start_time, "segundos")
    
    # Definir los límites del color para el trazado grueso de la trayectoria en HSV
    lower_bound = np.array([166, 100, 37])
    upper_bound = np.array([179, 255, 255])
    
    # Filtrar la imagen para resaltar los trazados gruesos de la trayectoria
    start_time = time.time()
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    print("Tiempo de procesamiento para filtrar la imagen:", time.time() - start_time, "segundos")
    
    # Aplicar el filtro morfológico para mejorar la forma de los trazados
    start_time = time.time()
    kernel = np.ones((7,7),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    print("Tiempo de procesamiento para aplicar el filtro morfológico:", time.time() - start_time, "segundos")

    # Aplicar la operación de erosión para adelgazar la línea
    start_time = time.time()
    eroded_mask = cv2.erode(mask, kernel, iterations=1)
    print("Tiempo de procesamiento para aplicar la erosión:", time.time() - start_time, "segundos")
    
    # Se aplica binarizacion de la mascara para obtener la imagen resultante
    start_time = time.time()
    result_image = np.zeros_like(eroded_mask)
    result_image[eroded_mask > 0] = 255  
    print("Tiempo de procesamiento para binarizar la máscara y convertir la imagen resultante a escala de grises:", time.time() - start_time, "segundos")

    start_time = time.time()

    # Aplicar el algoritmo de Thinning 

    #OPCION 1
    #result_image= cv2.ximgproc.thinning(result_image)

    #OPCION 2
    result_image=morph.skeletonize(result_image,method='zhang').astype(np.uint8) * 255

    print("Tiempo de procesamiento para adelgazar la imagen:", time.time() - start_time, "segundos")

    # Crear una copia de la imagen original para mostrar las partes blancas de la imagen mejorada
    start_time = time.time()
    overlay_image = original_image.copy()
    print("Tiempo de procesamiento para copiar la imagen original:", time.time() - start_time, "segundos")
    
    # Reemplazar los píxeles de la copia con los píxeles blancos de la imagen mejorada
    start_time = time.time()
    overlay_image[result_image == 255] = [255, 255, 255]
    print("Tiempo de procesamiento para reemplazar los píxeles de la copia:", time.time() - start_time, "segundos")
    
    # Redimensionar las imágenes para que se ajusten a la pantalla
    start_time = time.time()
    height, width = original_image.shape[:2]
    scale_factor = 0.5
    scaled_original = cv2.resize(original_image, (int(width*scale_factor), int(height*scale_factor)))
    scaled_result = cv2.resize(overlay_image, (int(width*scale_factor), int(height*scale_factor)))
    print("Tiempo de procesamiento para redimensionar las imágenes:", time.time() - start_time, "segundos")
    
    # Mostrar la imagen original y la imagen resultante
    cv2.imshow('Enhanced Image', scaled_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ruta de la imagen
image_path = 'foto1.jpg'

# Llamar a la función para filtrar y mejorar la imagen
filter_and_enhance(image_path)
