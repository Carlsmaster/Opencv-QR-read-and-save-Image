import numpy as np
import pyzbar.pyzbar as pyzbar
import os
import time
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Captura un frame de la cámara

    if ret:
        # Convierte el frame de OpenCV a escala de grises para la detección de QR
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Realiza la detección de códigos QR en el frame
        decoded_objects = pyzbar.decode(frame)

        for obj in decoded_objects:
            # Extrae el contenido del código QR
            qr_content = obj.data.decode('utf-8')

            # Define la ruta base
            base_path = "Ruta donde deseas almacenar la imagen"

            # Utiliza el contenido del código QR como nombre de archivo
            nombre_archivo = f"{qr_content}_Nombre de la imagen.png"

            # Ruta completa para guardar la imagen
            ruta_completa = os.path.join(base_path, nombre_archivo)

            # Guarda el frame actual como una imagen en la ruta especificada
            cv2.imwrite(ruta_completa, frame)
            print(f"Foto tomada y guardada como '{ruta_completa}'")

# Libera la cámara y cierra la ventana cuando termines
cap.release()
cv2.destroyAllWindows()