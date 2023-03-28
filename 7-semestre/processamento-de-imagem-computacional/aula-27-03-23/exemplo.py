from matplotlib import pyplot as plt
import cv2

im = cv2.imread("image.jpeg")

# convertendo imagem para cinza
# gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# cv2.imshow("teste", im)
# cv2.waitKey(0)

# Calculo de histograma de imagem em tons de cinza
# h = cv2.calcHist([gray_image], [0], None, [256], [0,256])

# plt.plot(h)
# plt.show()

## Calculo de canais por cor
# canais = cv2.split(im)

# cores = ("b", "g", "r")

# plt.figure()
# plt.title("histograma coloribo")
# plt.xlabel("intensidade")

# for (canal, cor) in zip(canais, cores):

#     #Este loop executa 3 vezes, uma para cada canal
#     hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
#     plt.plot(hist, color = cor)
#     plt.xlim([0, 256])

# plt.show()
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)



