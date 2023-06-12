import cv2
import numpy as np
from matplotlib import pyplot as plt


# Importando imagens ----------------------------->>>>>
IMAGE_PATH_ONE = "imagens/underexposure_gray.jpg"
IMAGE_PATH_TWO = "imagens/overexposure_gray.jpg"

img1_gray = cv2.imread(IMAGE_PATH_ONE)
img2_gray = cv2.imread(IMAGE_PATH_TWO)


# Primeira imagem GRAY - Underexposure ----------------------------->>>>>

# Criar a figura e os subplots:
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da primeira imagem GRAY sem tratamento no subplot (0, 0):
axs1[0, 0].imshow(img1_gray)
axs1[0, 0].set_title('Underexposure - Gray sem tratamento')
plt.subplot(2, 2, 1)
plt.imshow(img1_gray)

# Quantidade de pixels:
height1, width1, channels = img1_gray.shape

# Valor para alterar o brilho:
alpha_brilho = 30

# Somar com valor escalar aumenta o brilho:
img_gray1_brilho = img1_gray + alpha_brilho

# Exibição da primeira imagem GRAY com brilho aumentado no subplot (0, 1):
axs1[0, 1].imshow(img_gray1_brilho, cmap='gray')
axs1[0, 1].set_title('Underexposure - Gray com brilho aumentado')
plt.subplot(2, 2, 2)

# Colocando imagem em formato correto:
img_gray1_brilho = cv2.cvtColor(img_gray1_brilho, cv2.COLOR_BGR2GRAY)
img1_gray = cv2.cvtColor(img1_gray, cv2.COLOR_BGR2GRAY)

# Realiza a equalização do histograma:
img1_gray_equ = cv2.equalizeHist(img1_gray)
axs1[1, 0].imshow(img1_gray_equ, cmap='gray')
axs1[1, 0].set_title('Underexposure - Gray equalizada')

# EDIÇÃO DA IMAGEM:

# Ajuste de sombra:
clahe = cv2.createCLAHE(clipLimit=10, tileGridSize=(5, 5))
img_gray1_editada = clahe.apply(img_gray1_brilho)

# Aplicar desfoque:
img_gray1_editada = cv2.blur(img_gray1_editada, (3, 3), 15)

# Ajustar o contraste:
alpha = -1.2
beta = 10
img_gray1_editada = cv2.convertScaleAbs(img_gray1_editada, alpha=alpha, beta=beta)

# Salvando primeira imagem em GRAY editada:
output_path = 'imagens/underexposure_Editgray.jpg'
cv2.imwrite(output_path, img_gray1_editada)


# Exibição da primeira imagem GRAY editada no subplot (1, 1):
axs1[1, 1].imshow(img_gray1_editada, cmap='gray')
axs1[1, 1].set_title('Underexposure - Gray editada')

# Ajustar o layout dos subplots
plt.tight_layout()

# Exibe a imagem
plt.show()


# Segunda imagem - Overexposure ----------------------------->>>>>

# Criar a figura e os subplots:
fig2, axs2 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da segunda imagem GRAY sem tratamento no subplot (0, 0):
axs2[0, 0].imshow(img2_gray)
axs2[0, 0].set_title('Overexposure - Gray sem tratamento')

# Quantidade de pixels:
height2, width2, channels = img2_gray.shape

# Valor para alterar o brilho:
alpha_brilho = -50

# Somar com valor escalar aumenta o brilho:
img_gray2_brilho = img2_gray + alpha_brilho

# Exibição da segunda imagem GRAY com brilho aumentado no subplot (0, 1):
axs2[0, 1].imshow(img_gray2_brilho, cmap='gray')
axs2[0, 1].set_title('Overexposure - Gray com brilho diminuido')

# Colocando imagem em formato correto:
img2_gray = cv2.cvtColor(img2_gray, cv2.COLOR_BGR2GRAY)


# Realiza a equalização do histograma:
img2_gray_equ = cv2.equalizeHist(img2_gray)
axs2[1, 0].imshow(img2_gray_equ, cmap='gray')
axs2[1, 0].set_title('Overexposure - Gray equalizada')

# EDIÇÃO DA IMAGEM:

# Ajuste de sombra:
clahe = cv2.createCLAHE(clipLimit=30, tileGridSize=(8, 8))
img_gray2_editada = clahe.apply(img2_gray)

# Ajustar o contraste:
alpha = 1.0
beta = -40.0
img_gray2_editada = cv2.convertScaleAbs(img_gray2_editada, alpha=alpha, beta=beta)

# Ajustar foco:
img_gray2_editada = cv2.blur(img_gray2_editada, (3, 3), 5)

# Ajustar brilho:
brilho = 0.8
img_gray2_editada = np.clip(img_gray2_editada * brilho, 0, 255).astype(np.uint8)

# Salvando segunda imagem em GRAY editada:
output_path = 'imagens/overexposure_Editgray.jpg'
cv2.imwrite(output_path, img_gray2_editada)

# Exibição da segunda imagem GRAY editada no subplot (1, 1):
axs2[1, 1].imshow(img_gray2_editada, cmap='gray')
axs2[1, 1].set_title('Overexposure - Gray editada')

# Ajustar o layout dos subplots
plt.tight_layout()

# Exibição
plt.show()
