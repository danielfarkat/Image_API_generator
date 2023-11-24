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
import geopandas as gpd
# a melhor dica é poder trabalhar com o shapefile em dataframe usando o geopandas
# o geodataframe que é diferente do dataframe porque tem uma coluna chamada geometry e essa coluna é so poligono e o dataframe armazana as coordenadas e eu posso alterar de uma vez todo o sistema de coordenadas 
# aqui seram colocados três novas fuções a primeira terá o objetivo de fazer a comunicação com o S3

def s3_communication(day,month,year,MGRS_area):
    #esta função tem por objetivo comunicar com o S3, portanto terá que ser vinculada nosso sistema
    print(day,month,year,MGRS_area)

# Desativa a autenticação AWS
os.environ['AWS_NO_SIGN_REQUEST'] = 'YES'

def s3_shapefile_trim(forma, imagem_url):
    shapes = gpd.read_file(forma).to_crs("EPSG:32722")
    # aqui estou colocando a coordenada exata da ePSG que transforma o ponto de brasília como o equador ou seja rotacionado, desta forma o shape fica no msm formato da imagem.

        # Obtém o sistema de referência da imagem
    with rasterio.open(imagem_url) as src:
        dst_crs = src.crs

        # Transforma as geometrias do shapefile para o sistema de referência da imagem
    shapes_transformed = []
        # não usar o warp  para poder transformar de um raster para outra
        # não vou transformar o rester para o sistema do poligon vou transformar do poligon para o raster 
    '''
    for shape in shapes:
        # tem que trocar o warp por outra coisa nesse caso vou usar a biblioteca recomendada do geodataframe
        shape_transformed = warp.transform_geom(src_crs=shapefile.crs, dst_crs=dst_crs, geom=shape, antimeridian_cutting=True)
        shapes_transformed.append(shape_transformed)
    '''
    with rasterio.open(imagem_url) as src:
        # aqui eu tenho que perceber que o mask recebe uma geo e não um dataframe então tenho que trabalhar como se fosse uma geosérie.
        out_image, out_transform = rasterio.mask.mask(src, shapes.geometry)
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


