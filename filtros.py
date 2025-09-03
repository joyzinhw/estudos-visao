import cv2
import numpy as np
import matplotlib.pyplot as plt

def mostrar_comparacao(titulos, imagens):
    plt.figure(figsize=(15,5))
    for i, (titulo, img) in enumerate(zip(titulos, imagens)):
        plt.subplot(1, len(imagens), i+1)
        if len(img.shape) == 2:
            plt.imshow(img, cmap="gray")
        else:
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title(titulo)
        plt.axis("off")
    plt.show()

img = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3), np.float32) / 9  

conv_replicate = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_REPLICATE)
mostrar_comparacao(
    ["Original", "Convolução - Replicação",],
    [img, conv_replicate]
)

img_ruido = cv2.imread("lena2.jpg", cv2.IMREAD_GRAYSCALE)

filtro_media = cv2.blur(img_ruido, (3,3))
filtro_mediana = cv2.medianBlur(img_ruido, 3)

mostrar_comparacao(
    ["Original com Ruído", "Filtro da Média 3x3", "Filtro da Mediana 3x3"],
    [img_ruido, filtro_media, filtro_mediana]
)
img4 = cv2.imread("lena3.png", cv2.IMREAD_GRAYSCALE)

filtro_max = cv2.dilate(img4, np.ones((3,3), np.uint8))


filtro_min = cv2.erode(img4, np.ones((3,3), np.uint8))

mostrar_comparacao(
    ["Original", "Filtro Máximo (destaca claras)", "Filtro Mínimo (destaca escuras)"],
    [img4, filtro_max, filtro_min]
)

img3 = cv2.imread("FILTRAGEM.png", cv2.IMREAD_GRAYSCALE)

blur = cv2.GaussianBlur(img3, (5,5), 1)
mask = cv2.subtract(img3, blur)
k = 1.5
high_boost = cv2.addWeighted(img3, 1.0 + k, blur, -k, 0)

mostrar_comparacao(
    ["Original", "Máscara (Detalhes)", f"High-Boost k={k}"],
    [img3, mask, high_boost]
)
