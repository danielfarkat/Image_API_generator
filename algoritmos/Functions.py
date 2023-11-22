import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def obter_imagens_satelite(latitude, longitude, data_inicio, data_fim):
    # URL base para as imagens de satélite do USGS
    url_base = "https://earthexplorer.usgs.gov"

    # Fazer uma solicitação para a página de pesquisa do Earth Explorer
    pesquisa_url = f"{url_base}/search"
    parametros_pesquisa = {
        "lat": latitude,
        "lon": longitude,
        "startDate": data_inicio,
        "endDate": data_fim,
    }
    resposta_pesquisa = requests.get(pesquisa_url, params=parametros_pesquisa)
    print(resposta_pesquisa)

    # Verificar se a solicitação foi bem-sucedida
    if resposta_pesquisa.status_code == 200:
        # Analisar a página de pesquisa para obter o link da imagem
        soup = BeautifulSoup(resposta_pesquisa.text, "html.parser")
        link_imagem = soup.find("a", class_="thumbnail")["href"]

        # Construir a URL completa da imagem
        url_imagem = f"{url_base}{link_imagem}"

        # Fazer uma solicitação para a página da imagem
        resposta_imagem = requests.get(url_imagem)

        # Verificar se a solicitação foi bem-sucedida
        if resposta_imagem.status_code == 200:
            # Extrair informações da imagem
            informacoes_imagem = soup.find("div", class_="additional-fields").text.strip()

            # Baixar a imagem
            imagem_bytes = BytesIO(resposta_imagem.content)
            imagem = Image.open(imagem_bytes)

            # Retornar a imagem e as informações
            return imagem, informacoes_imagem
        else:
            print(f"Erro ao obter a imagem. Código de status: {resposta_imagem.status_code}")
    else:
        print(f"Erro ao fazer a pesquisa. Código de status: {resposta_pesquisa.status_code}")


