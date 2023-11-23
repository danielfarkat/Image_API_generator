# Considerações:

- A API aqui solicitada nescessita de uma chave de acesso, por tal motivo irei comitar esta chave no .ignore e portanto criei uma pasta chamada passoword.py e criei da seguinte forma suas chaves de acesso

```
EE_USER="user_name"
EE_PASS="user_pass"
```

# Consideração:

- Existe a opção de utilizar o banco de dados salvo em nuvem da plataforma AWS da amazon, neste caso é possível utilizar o banco de dados [Sentinel-cogs](https://registry.opendata.aws/sentinel-2-l2a-cogs/)

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
