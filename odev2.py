# Salih Türkoğlu 02205076023
import cv2
import numpy as np
invFoto=cv2.imread('resim.jpeg')
foto=cv2.imread('resim.jpeg',0)
cv2.imshow('Hatalet',foto)
[h,w]=foto.shape
invFoto=np.zeros([h,w],dtype=np.uint8)

for u in range(h):
    for v in range(w):
        invFoto[u,v]=255-foto[u,v]

cv2.imshow("Ters Hayalet",invFoto)
print(invFoto)
print(50*"-")
print(foto)
cv2.waitKey()