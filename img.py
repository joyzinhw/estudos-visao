#visualizar img
import cv2
img = cv2.imread('img/eletro.jpeg') # entrada
cv2.imshow('eletro', img) # legenda
cv2.waitKey(0)
cv2.destroyAllWindows()  #saida

# #converter img

cv2.imwrite("imgeletro.jpg", img)

#Redimensionamento de Imagem

img = cv2.imread('eletroteste.png')

# Redimensionar para 300x300 pixels
resized = cv2.resize(img, (300, 300))

# Exibir a imagem
cv2.imshow('Redimensionada', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem em Escala de Cinza', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Filtro de Suavização (Blur)
blurred = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Imagem Suavizada', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Detecção de Bordas
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Detecção de Bordas', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
