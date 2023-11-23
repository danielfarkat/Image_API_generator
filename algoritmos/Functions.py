import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import fiona
import rasterio
import rasterio.mask
from matplotlib import pyplot as plt
from osgeo import gdal
from rasterio.session import AWSSession
import os
from rasterio import warp

# aqui seram colocados três novas fuções a primeira terá o objetivo de fazer a comunicação com o S3

def s3_communication(day,month,year,MGRS_area):
    #esta função tem por objetivo comunicar com o S3, portanto terá que ser vinculada nosso sistema
    print(day,month,year,MGRS_area)

# Desativa a autenticação AWS
os.environ['AWS_NO_SIGN_REQUEST'] = 'YES'

def s3_shapefile_trim(forma, imagem_url):
    with fiona.open(forma, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

        # Obtém o sistema de referência da imagem
        with rasterio.open(imagem_url) as src:
            dst_crs = src.crs

        # Transforma as geometrias do shapefile para o sistema de referência da imagem
        shapes_transformed = []
        for shape in shapes:
            shape_transformed = warp.transform_geom(src_crs=shapefile.crs, dst_crs=dst_crs, geom=shape, antimeridian_cutting=True)
            shapes_transformed.append(shape_transformed)

    with rasterio.open(imagem_url) as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes_transformed, invert=False)
        out_meta = src.meta
        out_meta.update({
            "driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform
        })

    with rasterio.open("RGB.byte.masked.tif", "w", **out_meta) as dest:
        dest.write(out_image)




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


