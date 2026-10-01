import numpy as np
import cv2
# vision artificial act10 NC = 0072
# Lee la imagen en escala de grises
img = cv2.imread("tamsy.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("tamsy 0072", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# linea
print(" La linea 0072")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow(" la line 0072", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# el circulo
print(" el circulo 0072")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen
cv2.imshow("el circulo 0072", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# el texto 
print(" el texto 0072")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "circulo y linea", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
# Abre la ventana con la imagen
cv2.imshow("el circulo 0072", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#los Trackbars 
print("los trackbars 0072")
def on_trackbar(val):
  print(val)

# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R','frame',0,255,on_trackbar)
cv2.createTrackbar('G','frame',0,255,on_trackbar)
cv2.createTrackbar('B','frame',0,255,on_trackbar)

while(True):
    cv2.imshow('frame',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R','frame')
    g = cv2.getTrackbarPos('G','frame')
    b = cv2.getTrackbarPos('B','frame')

    img[:] = [b,g,r]

cv2.destroyAllWindows()

# los Thresholding
print("los Thresholding 0072")

nCam = 0

# Abrir la cámara
cap = cv2.VideoCapture(nCam, cv2.CAP_DSHOW)

# Verificar que la cámara se abrió correctamente
if not cap.isOpened():
    print("ERROR: No se pudo abrir la cámara.")
    print("Prueba con nCam = 1, 2, etc.")
    exit()

cv2.namedWindow('frame1')
cv2.moveWindow('frame1', 30, 100)

cv2.namedWindow('frame2')
cv2.moveWindow('frame2', 700, 100)

cv2.namedWindow('frame3')
cv2.moveWindow('frame3', 365, 150)

lower_color = np.array([155, 80, 80])
upper_color = np.array([175, 255, 255])

while True:

    ret, frame = cap.read()

    # Verificar que realmente recibimos un frame
    if not ret or frame is None:
        print("ERROR: No se pudo leer un frame de la cámara.")
        break

    # Convertimos la imagen de BGR a HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Máscara: blanco para el rango seleccionado, negro para el resto
    mask_color = cv2.inRange(
        hsv_frame,
        lower_color,
        upper_color
    )

    # Aplicamos la máscara a la imagen original
    hsv_frame_mask = cv2.bitwise_and(
        frame,
        frame,
        mask=mask_color
    )

    cv2.imshow('frame1', frame)
    cv2.imshow('frame2', hsv_frame_mask)
    cv2.imshow('frame3', mask_color)

    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("catherine eileen huerta rascon NC = 0072")