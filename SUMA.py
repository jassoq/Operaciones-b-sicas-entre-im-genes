import cv2
import numpy as np
from ctypes import c_float

def norm(c_float):
    c_float = c_float - np.min(c_float)
    c_float = c_float / np.max(c_float)
    return c_float

img1 = cv2.imread('IMG1.jpg')
img2 = cv2.imread('IMG2.jpg')
img1_float = img1.astype (np.int32)
img2_float = img2.astype (np.int32)


suma = img1_float + img2_float
suma = norm (suma)
suma = suma * 255
s = suma.astype(np.uint8)
cv2.imshow("SUMA",s)

cv2.waitKey(0)
cv2.destroyAllWindows()



''' Con funciones ya definidad


import cv2

#Se leen las imagenes
img1 = cv2.imread('IMG1.jpg')
img2 = cv2.imread('IMG2.jpg')

# utilizamos la función cv2.add, en ella especificamos img1 e img2 correspondientes a las imágenes leídas.
#IMG = cv2.add(img1,img2)

IMG= img1 + img2

#Visualizamos los resultados
cv2.imshow('IMG',IMG)

cv2.waitKey(0)
cv2.destroyAllWindows()

###

import cv2

# donde estamos leyendo directamente en escala de grises al ubicar 0
img1 = cv2.imread('IMG1.jpg',0)
img2 = cv2.imread('IMG2.jpg',0)

IMG = cv2.add(img1,img2)

#usamos print para obtener el primer elemento de cada imagen
print('img1[0,0]= ', img1[0,0])
print('img2[0,0]= ', img2[0,0])
print('IMG[0,0]= ', IMG[0,0])

cv2.imshow('IMG',IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Entonces si sumamos 65 y 226, tenemos un total de 291, sin embargo, 
#vemos que en resA[0,0] obtenemos 255, esto es debido a que al usar cv2.add si la suma excede a 255, el valor vuelve a 255.
'''
