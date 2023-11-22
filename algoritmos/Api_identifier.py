import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from Functions import obter_imagens_satelite

if __name__ == "__main__":
    # Exemplo de uso
    latitude = 37.7749
    longitude = -122.4194
    data_inicio = "2022-01-01"
    data_fim = "2022-12-31"

    imagem, informacoes = obter_imagens_satelite(latitude, longitude, data_inicio, data_fim)

    # Exibir a imagem e informações
    imagem.show()
    print("Informações da imagem:")
    print(informacoes)
