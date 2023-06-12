# Atividade feita seguindo instruções e o nome dado pela faculdade para cada imagem.

import cv2
import matplotlib.pyplot as plt

# Importando imagens ----------------------------->>>>>
IMAGE_PATH_ONE = "imagens/underexposure.jpg"
IMAGE_PATH_TWO = "imagens/overexposure.jpg"

img1 = cv2.imread(IMAGE_PATH_ONE)
img2 = cv2.imread(IMAGE_PATH_TWO)


# Primeira imagem - Underexposure ----------------------------->>>>>

# Para RGB:
img_rgb1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# Salvando primeira imagem em RGB:
output_path = 'imagens/underexposure_rgb.jpg'
cv2.imwrite(output_path, img_rgb1)

# Criar a figura e os subplots:
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da primeira imagem RGB no subplot (0, 0):
axs1[0, 0].imshow(img_rgb1)
axs1[0, 0].set_title('Underexposure - RGB')
plt.subplot(2, 2, 1)

# Para Gray Scale:
img_gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Exibição da primeira imagem GRAY no subplot (0, 1)
axs1[0, 1].imshow(img_gray1, cmap='gray')
axs1[0, 1].set_title('Underexposure - Grayscale')
plt.subplot(2, 2, 3)

# Salvando primeira imagem em GRAY:
output_path = 'imagens/underexposure_gray.jpg'
cv2.imwrite(output_path, img_gray1)

# Dados da imagem ----------------------------->>>>>
print("Imagem 1:")

# Média de iluminância:
imagem_cinza1 = img_gray1.mean()
print("Média de iluminância/nível de cinza: ", imagem_cinza1)

# Quantidade de pixels:
height1, width1, channels = img1.shape
pixel_count1 = width1 * height1
print("Quantidade de pixels: ", pixel_count1, "Tamanho da imagem: ", width1, "X", height1)

# Calcular o histograma:
range_hist = [0, 256]
hist1, bins1, _ = plt.hist(img_gray1.ravel(), bins=width1, range=range_hist)

# Exibir o histograma no subplot (1, 0):
axs1[1, 0].plot(bins1[:-1], hist1)
axs1[1, 0].set_xlabel('Níveis de Cinza')
axs1[1, 0].set_ylabel('Contagem')
axs1[1, 0].set_title('Histograma da imagem 1')

# Remover os eixos dos subplots vazios
axs1[1, 1].axis('off')

# Ajustar o layout dos subplots
plt.tight_layout()


#Segunda imagem - Overexposure ----------------------------->>>>>

# Para RGB:
img_rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Salvando segunda imagem em RGB:
output_path = 'imagens/overexposure_rgb.jpg'
cv2.imwrite(output_path, img_rgb2)

# Criar a figura e os subplots:
fig2, axs2 = plt.subplots(2, 2, figsize=(10, 10))

# Exibição da segunda imagem RGB no subplot (0, 0):
axs2[0, 0].imshow(img_rgb2)
axs2[0, 0].set_title('Overexposure - RGB')
plt.subplot(2, 2, 1)

# Para Gray Scale:
img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Exibição da segunda imagem GRAY no subplot (0, 1):
axs2[0, 1].imshow(img_gray2, cmap='gray')
axs2[0, 1].set_title('Overexposure - Grayscale')
plt.subplot(2, 2, 3)

# Salvando segunda imagem em GRAY:
output_path = 'imagens/overexposure_gray.jpg'
cv2.imwrite(output_path, img_gray2)

# Dados da imagem ----------------------------->>>>>
print("Imagem 2:")

# Média de iluminância:
imagem_cinza2 = img_gray2.mean()
print("Média de iluminância/nível de cinza: ", imagem_cinza2)

# Quantidade de pixels:
height2, width2, channels = img2.shape
pixel_count2 = width2 * height2
print("Quantidade de pixels: ", pixel_count2, "Tamanho da imagem: ", width2, "X", height2)

# Calcular o histograma:
range_hist = [0, 256]
hist2, bins2, _ = plt.hist(img_gray2.ravel(), bins=width2, range=range_hist)

# Exibir o histograma no subplot (1, 0):
axs2[1, 0].plot(bins2[:-1], hist2)
axs2[1, 0].set_xlabel('Níveis de Cinza')
axs2[1, 0].set_ylabel('Contagem')
axs2[1, 0].set_title('Histograma da imagem 2')

# Remover os eixos dos subplots vazios
axs2[1, 1].axis('off')

# Ajustar o layout dos subplots
plt.tight_layout()

# Exibir a figura com os subplots
plt.show()








