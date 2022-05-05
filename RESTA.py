import cv2
import numpy as np
from ctypes import c_float

def norm(c_float):
    c_float = c_float - np.min(c_float)
    c_float = c_float / np.max(c_float)
    return c_float

#img1 = cv2.imread("IMG1.jpg")
#img2 = cv2.imread("IMG2.jpg")

img1 = cv2.imread("IMG1.jpg",0)
img2 = cv2.imread("IMG2.jpg",0)
img1_float = img1.astype (np.int32)
img2_float = img2.astype (np.int32)


resta = img1_float - img2_float
resta = norm (res)
resta = res * 255
resultado= res.astype(np.uint8)
cv2.imshow("RESTA",resultado)

print('img1[0,0]= ', img1[0,0])
print('img2[0,0]= ',img2[0,0])
print('resultado2[0,0]= ',resultado[0,0])

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
import cv2

#Aquí leemos las imágenes que hemos venido utilizando, especificando 0 para leerlas directamente en escala de grises
img1 = cv2.imread('IMG1.jpg',0)
img2 = cv2.imread('IMG2.jpg',0)

resultado = cv2.subtract(img1,img2)

print('img1[0,0]= ',img1[0,0])
print('img2[0,0]= ',img2[0,0])
print('resultado[0,0]= ',resultado[0,0])

cv2.imshow('resultado',resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Con el resultado si restamos 65 – 226, tenemos un total de -161, sin embargo, 
#vemos que en resultado[0,0] se obtiene 0, esto es debido a que al usar cv2.subtract si el resultado es menor a 0, el valor vuelve a 0.


import cv2

img1 = cv2.imread('IMG1.jpg',0)
img2 = cv2.imread('IMG2.jpg',0)

resultado2 = cv2.absdiff(img1,img2)

#cv2.absdif calcula la diferencia en el valor absoluto Una vez teniendo el valor absoluto |-161| lo cambia a 161

print('img1[0,0]= ', img1[0,0])
print('img2[0,0]= ',img2[0,0])
print('resultado2[0,0]= ',resultado2[0,0])

cv2.imshow('resultado2',resultado2)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
