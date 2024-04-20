import cv2
import numpy as np
import time
import skimage.morphology as morph

def filter_and_enhance(video_path):
    # Abrir el archivo de video
    cap = cv2.VideoCapture(video_path)
    
    # Obtener el ancho, el alto y la velocidad de fotogramas del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Crear un objeto VideoWriter para guardar el video resultante
    out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Tiempo del último fotograma capturado
    last_frame_time = 0

    while cap.isOpened():
        # Leer el tiempo actual
        current_time = time.time()
        
        # Leer el siguiente fotograma del video
        ret, frame = cap.read()

        if not ret:
            break
        
        # Capturar un fotograma cada 0.1 segundos
        if current_time - last_frame_time >= 0.1:
            # Actualizar el tiempo del último fotograma capturado
            last_frame_time = current_time

            # Convertir el fotograma a espacio de color HSV
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # Definir los límites del color para el trazado grueso de la trayectoria en HSV
            lower_bound = np.array([166, 100, 37])
            upper_bound = np.array([179, 255, 255])
            
            # Filtrar el fotograma para resaltar los trazados gruesos de la trayectoria
            mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
            
            # Aplicar el filtro morfológico para mejorar la forma de los trazados
            kernel = np.ones((7,7),np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # Aplicar la operación de erosión para adelgazar la línea
            eroded_mask = cv2.erode(mask, kernel, iterations=1)
            
            # Aplicar binarización de la máscara para obtener el fotograma resultante
            result_frame = np.ones_like(frame) * 255
            result_frame[eroded_mask == 0] = 0
            result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2GRAY)

            result_frame=morph.skeletonize(result_frame,method='zhang').astype(np.uint8) * 255


            # Crear una copia del fotograma original para mostrar las partes blancas del fotograma mejorado
            overlay_frame = frame.copy()
            
            # Reemplazar los píxeles de la copia con los píxeles blancos del fotograma mejorado
            overlay_frame[result_frame == 255] = [255, 255, 255]
            
            # Escribir el fotograma procesado en el video de salida
            out.write(overlay_frame)

            # Calcular y mostrar el porcentaje de progreso
            current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            percentage = (current_frame / total_frames) * 100
            print(f'Procesando: {percentage:.2f}% completado', end='\r')

    # Liberar los recursos y cerrar todas las ventanas
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Ruta del video
video_path = 'video_low_resolution.mp4'

# Llamar a la función para filtrar y mejorar el video
filter_and_enhance(video_path)
