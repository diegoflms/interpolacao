import numpy as np
from PIL import Image


class Zoom:
    def __init__(self):
        pass

    # Função para dar zoom em uma área central da imagem
    def run(self,img_np_array, zoom_factor):
        # Abrir a imagem
        img = Image.fromarray(img_np_array)

        # Calcular as dimensões da área central
        width, height = img.size
        center_x, center_y = width // 2, height // 2

        # Determinar a nova largura e altura com base no fator de zoom
        zoom_width = int(width / zoom_factor)
        zoom_height = int(height / zoom_factor)

        # Definir a caixa de recorte (crop box)
        left = center_x - zoom_width // 2
        top = center_y - zoom_height // 2
        right = center_x + zoom_width // 2
        bottom = center_y + zoom_height // 2

        # Cortar a imagem para obter a região do zoom
        cropped_img = img.crop((left, top, right, bottom))

        # Redimensionar a imagem cortada ao tamanho original utilizando interpolação bilinear
        resized_img = cropped_img.resize((width, height), Image.BILINEAR)

        return np.array(resized_img)
