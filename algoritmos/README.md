# Considerações:

- A API aqui solicitada nescessita de uma chave de acesso, por tal motivo irei comitar esta chave no .ignore e portanto criei uma pasta chamada passoword.py e criei da seguinte forma suas chaves de acesso

```
EE_USER="user_name"
EE_PASS="user_pass"
```

- Existe a opção de utilizar o banco de dados salvo em nuvem da plataforma AWS da amazon, neste caso é possível utilizar o banco de dados [Sentinel-cogs](https://registry.opendata.aws/sentinel-2-l2a-cogs/)

# Listar

```
aws s3 ls --no-sign-request s3://sentinel-cogs/sentinel-s2-l2a-cogs/22/L/HH/2023/7/S2A_22LHH_20230703_0_L2A/
```

- Importante ressaltar que o sistema de referência dosentinel é do tipo MGRS e tal sistema é utilzado pelo satélite sentinel 2 neste sistema o mundo é divido em quadrante de 100 x 100 km e desta forma é possível somente passar o quadrante para poder descobrir a localização em que temos a seguinte orientação de informação

```
NumNum/string/stringstring

para o exemplo é

22/L/HH
```

- Após realizar este projeto é possível realizar o download de arquivo

# Acessar informações do observador

- request

```
AWS_NO_SIGN_REQUEST=YES gdalinfo /vsis3/sentinel-cogs/sentinel-s2-l2a-cogs/22/L/HH/2023/7/S2A_22LHH_20230703_0_L2A/B04.tif
```

- resposta

```

Driver: GTiff/GeoTIFF
Files: /vsis3/sentinel-cogs/sentinel-s2-l2a-cogs/22/L/HH/2023/7/S2A_22LHH_20230703_0_L2A/B04.tif
Size is 10980, 10980
Coordinate System is:
PROJCRS["WGS 84 / UTM zone 22S",
    BASEGEOGCRS["WGS 84",
        DATUM["World Geodetic System 1984",
            ELLIPSOID["WGS 84",6378137,298.257223563,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        ID["EPSG",4326]],
    CONVERSION["UTM zone 22S",
        METHOD["Transverse Mercator",
            ID["EPSG",9807]],
        PARAMETER["Latitude of natural origin",0,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8801]],
        PARAMETER["Longitude of natural origin",-51,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8802]],
        PARAMETER["Scale factor at natural origin",0.9996,
            SCALEUNIT["unity",1],
            ID["EPSG",8805]],
        PARAMETER["False easting",500000,
            LENGTHUNIT["metre",1],
            ID["EPSG",8806]],
        PARAMETER["False northing",10000000,
            LENGTHUNIT["metre",1],
            ID["EPSG",8807]]],
    CS[Cartesian,2],
        AXIS["(E)",east,
            ORDER[1],
            LENGTHUNIT["metre",1]],
        AXIS["(N)",north,
            ORDER[2],
            LENGTHUNIT["metre",1]],
    USAGE[
        SCOPE["Engineering survey, topographic mapping."],
        AREA["Between 54°W and 48°W, southern hemisphere between 80°S and equator, onshore and offshore. Brazil. Uruguay."],
        BBOX[-80,-54,0,-48]],
    ID["EPSG",32722]]
Data axis to CRS axis mapping: 1,2
Origin = (799980.000000000000000,8300020.000000000000000)
Pixel Size = (10.000000000000000,-10.000000000000000)
Metadata:
  AREA_OR_POINT=Area
  OVR_RESAMPLING_ALG=AVERAGE
Image Structure Metadata:
  COMPRESSION=DEFLATE
  INTERLEAVE=BAND
  PREDICTOR=2
Corner Coordinates:
Upper Left  (  799980.000, 8300020.000) ( 48d12'21.32"W, 15d21'32.66"S)
Lower Left  (  799980.000, 8190220.000) ( 48d11'32.03"W, 16d21' 1.91"S)
Upper Right (  909780.000, 8300020.000) ( 47d11' 4.67"W, 15d20'38.12"S)
Lower Right (  909780.000, 8190220.000) ( 47d 9'57.46"W, 16d20' 3.66"S)
Center      (  854880.000, 8245120.000) ( 47d41'13.87"W, 15d50'51.30"S)
Band 1 Block=1024x1024 Type=UInt16, ColorInterp=Gray
  NoData Value=0
  Overviews: 5490x5490, 2745x2745, 1373x1373, 687x687


```

# NDVI da série temporal

- Primeira análise, periodo de junho.

```
                           PRE S2A_22LHH_20230703_0_L2A/
                           PRE S2A_22LHH_20230706_0_L2A/
                           PRE S2A_22LHH_20230713_0_L2A/
                           PRE S2A_22LHH_20230716_0_L2A/
                           PRE S2A_22LHH_20230723_0_L2A/
                           PRE S2A_22LHH_20230726_0_L2A/
                           PRE S2B_22LHH_20230701_0_L2A/
                           PRE S2B_22LHH_20230708_0_L2A/
                           PRE S2B_22LHH_20230711_0_L2A/
                           PRE S2B_22LHH_20230718_0_L2A/
                           PRE S2B_22LHH_20230721_0_L2A/
                           PRE S2B_22LHH_20230728_0_L2A/
                           PRE S2B_22LHH_20230731_0_L2A/


```

# Como baixar o Shapefile

- É possível baixa o shapefile referente ao sistema de referência do sentinel 2 sobre o brasil a partir do site [InstrutorGIS](https://www.instrutorgis.com.br/download-da-grade-do-satelite-sentinel2/)
