import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('foto1.jpg')

# Rango de color de la cinta en HSV (valores iniciales)
lower_color = np.array([161, 110, 50])
upper_color = np.array([179, 255, 140])

# Función de callback para actualizar los valores HSV
def update_hsv(*args):
    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Actualizar la máscara con los nuevos valores HSV
    lower_color[0] = cv2.getTrackbarPos('Hue min', 'Color Adjustment')
    upper_color[0] = cv2.getTrackbarPos('Hue max', 'Color Adjustment')
    lower_color[1] = cv2.getTrackbarPos('Saturation min', 'Color Adjustment')
    upper_color[1] = cv2.getTrackbarPos('Saturation max', 'Color Adjustment')
    lower_color[2] = cv2.getTrackbarPos('Value min', 'Color Adjustment')
    upper_color[2] = cv2.getTrackbarPos('Value max', 'Color Adjustment')

    mask = cv2.inRange(hsv, lower_color, upper_color)
    cv2.imshow('Mask', mask)

# Crear una ventana para ajustar los valores HSV
cv2.namedWindow('Color Adjustment', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Mask', 400, 400)  # Redimensionar la ventana de la máscara

# Crear barras de desplazamiento para ajustar los valores HSV
cv2.createTrackbar('Hue min', 'Color Adjustment', lower_color[0], 179, update_hsv)
cv2.createTrackbar('Hue max', 'Color Adjustment', upper_color[0], 179, update_hsv)
cv2.createTrackbar('Saturation min', 'Color Adjustment', lower_color[1], 255, update_hsv)
cv2.createTrackbar('Saturation max', 'Color Adjustment', upper_color[1], 255, update_hsv)
cv2.createTrackbar('Value min', 'Color Adjustment', lower_color[2], 255, update_hsv)
cv2.createTrackbar('Value max', 'Color Adjustment', upper_color[2], 255, update_hsv)

# Mostrar la máscara inicial
mask = cv2.inRange(image, lower_color, upper_color)
cv2.imshow('Mask', mask)

# Mantener abierta la ventana hasta que se presione 'q'
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Almacenar los valores HSV seleccionados antes de salir
        lower_hue = cv2.getTrackbarPos('Hue min', 'Color Adjustment')
        upper_hue = cv2.getTrackbarPos('Hue max', 'Color Adjustment')
        lower_saturation = cv2.getTrackbarPos('Saturation min', 'Color Adjustment')
        upper_saturation = cv2.getTrackbarPos('Saturation max', 'Color Adjustment')
        lower_value = cv2.getTrackbarPos('Value min', 'Color Adjustment')
        upper_value = cv2.getTrackbarPos('Value max', 'Color Adjustment')

        # Devolver los valores HSV seleccionados
        print("Valores HSV seleccionados:")
        print("Hue min:", lower_hue)
        print("Hue max:", upper_hue)
        print("Saturation min:", lower_saturation)
        print("Saturation max:", upper_saturation)
        print("Value min:", lower_value)
        print("Value max:", upper_value)
        
        break

cv2.destroyAllWindows()
