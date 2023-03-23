import cv2;

imagem = cv2.imread("image.jpeg")

print(imagem.shape[1]) # Largura da imagem

print(imagem.shape[0]) # altura da imagem


(r,g,b) = cv2.split(imagem)

(r1,g1,b1) = imagem[0,0]


print(f"r1: {r1} g1? {g1} b1: {b1}")

blueimage = imagem.copy()
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        blueimage[y, x] = (255,0,0)
cv2.imshow("Imagem modificada", blueimage)
cv2.waitKey(0)

imagem2 = imagem.copy()

imagem2[30:50, :] = (255, 0, 0)

cv2.imshow("teste", imagem2)
cv2.waitKey(0)

cv2.imshow("Nome da janela", g)
cv2.waitKey(0)

cv2.imwrite("saida.jpg", imagem)