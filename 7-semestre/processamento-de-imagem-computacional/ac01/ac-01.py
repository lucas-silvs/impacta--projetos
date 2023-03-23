import cv2
import numpy as np
img = cv2.imread("5-dogs.jpg")

mascara = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.rectangle(mascara, (40, 170), (550,370), 255, -1)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)
cv2.imshow("Mascara aplicada a imagem", img_com_mascara)
cv2.waitKey(0)





