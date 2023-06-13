import cv2
import numpy as np
from matplotlib import pyplot as plt


# Importando imagens ----------------------------->>>>>
IMAGE_PATH_ONE = "imagens/underexposure_rgb.jpg"
IMAGE_PATH_TWO = "imagens/overexposure_rgb.jpg"

img1_rgb = cv2.imread(IMAGE_PATH_ONE)
img2_rgb = cv2.imread(IMAGE_PATH_TWO)

# Primeira imagem RGB - Underexposure ----------------------------->>>>>

# Criar a figura e os subplots:
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da primeira imagem RGB sem tratamento no subplot (0, 0):
axs1[0, 0].imshow(img1_rgb)
axs1[0, 0].set_title('Underexposure - RGB sem tratamento')
plt.subplot(2, 2, 1)
plt.imshow(img1_rgb)

# Quantidade de pixels:
height1, width1, channels = img1_rgb.shape

# Ajustar o brilho da imagem:
brilho = 1.5
img1_rgb_brilho = cv2.addWeighted(img1_rgb, brilho, np.zeros(img1_rgb.shape, dtype=np.uint8), 0, 0)

# Exibição da primeira imagem RGB com brilho aumentado no subplot (0, 1):
axs1[0, 1].imshow(img1_rgb_brilho)
axs1[0, 1].set_title('Underexposure - RGB com brilho aumentado')
plt.subplot(2, 2, 2)

# EDIÇÃO DA IMAGEM:

# Ajustar o brilho da imagem:
brilho = 5.0
img1_rgb_editada = cv2.addWeighted(img1_rgb, brilho, np.zeros(img1_rgb.shape, dtype=np.uint8), 0, 0)

# Aplicar o filtro de desfoque para suavizar a imagem
img1_rgb_editada = cv2.blur(img1_rgb_editada, (4, 4), 10)

# Ajustar o contraste
alpha = 1.2
beta = 10
img1_rgb_editada = cv2.convertScaleAbs(img1_rgb_editada, alpha=alpha, beta=beta)

# Exibição da primeira imagem RGB editada no subplot (1, 1):
axs1[1, 0].imshow(img1_rgb_editada)
axs1[1, 0].set_title('Underexposure - RGB editada')

# Ajustar o layout dos subplots
plt.tight_layout()

# Exibe a imagem
plt.show()


# Segunda imagem - Overexposure ----------------------------->>>>>

# Criar a figura e os subplots:
fig2, axs2 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da segunda imagem RGB sem tratamento no subplot (0, 0):
axs2[0, 0].imshow(img2_rgb)
axs2[0, 0].set_title('Overexposure - RGB sem tratamento')

# Quantidade de pixels:
height2, width2, channels = img2_rgb.shape

# Ajustar o brilho da imagem:
brilho = 50
img2_rgb_brilho = np.clip(img2_rgb.astype(int) - brilho, 0, 255).astype(np.uint8)


# Exibição da primeira imagem RGB com brilho aumentado no subplot (0, 1):
axs2[0, 1].imshow(img2_rgb_brilho)
axs2[0, 1].set_title('Overexposure - RGB com brilho diminuido')


# EDIÇÃO DA IMAGEM:

# Ajuste de brilho:
brilho = 200
img2_rgb_editada = np.clip(img2_rgb.astype(int) - brilho, 0, 255).astype(np.uint8)

# Aumentar o branco da imagem:
valor_clareamento = 1.0  # Fator de clareamento
img2_rgb_editada = np.clip(img2_rgb_editada * valor_clareamento, 0, 255).astype(np.uint8)

# Ajustar o contraste
alpha = 5.0
beta = -70
img2_rgb_editada = cv2.convertScaleAbs(img2_rgb_editada, alpha=alpha, beta=beta)

# Exibição da segunda imagem RGB editada no subplot (1, 1):
axs2[1, 1].imshow(img2_rgb_editada)
axs2[1, 1].set_title('Overexposure - RGB editada')

# Ajustar o layout dos subplots
plt.tight_layout()

# Exibição
plt.show()
