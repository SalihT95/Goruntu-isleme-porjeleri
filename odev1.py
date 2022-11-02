# Salih Türkoğlu 02205076023
import cv2
import numpy as np
foto = cv2.imread("doge.jpg")
cv2.imshow('Doge', foto)
islenmisFoto= cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gri Doge', islenmisFoto)
L=2**8
Hist=np.zeros(shape=(L,1))
size_y = islenmisFoto.shape[0]
size_x = islenmisFoto.shape[1]

for v in range(size_y):
    for u in range(size_x):
        i = islenmisFoto[u,v]
        Hist[i,0] = Hist[i,0]+1

import matplotlib.pyplot as plt
plt.xlabel('Pixel')
plt.ylabel('Adet')
plt.title('Doge Histogram')
plt.plot(Hist, color='purple')
plt.show()
cv2.waitKey()