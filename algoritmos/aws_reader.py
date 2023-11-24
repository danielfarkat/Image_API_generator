from Functions import det_data as s3_trim

padrao = "/vsis3/sentinel-cogs/sentinel-s2-l2a-cogs/22/L/HH/2023/7/S2B_22LHH_20230703_0_L2A/B04.tif"
banda='B04'
s3_trim(3,padrao,'A',banda)
s3_trim(6,padrao,'A',banda)
s3_trim(1,padrao,'B',banda)
s3_trim(8,padrao,'B',banda)
padrao = "/vsis3/sentinel-cogs/sentinel-s2-l2a-cogs/22/L/HH/2023/7/S2B_22LHH_20230703_0_L2A/B08.tif"
banda='B08'
s3_trim(3,padrao,'A',banda)
s3_trim(6,padrao,'A',banda)
s3_trim(1,padrao,'B',banda)
s3_trim(8,padrao,'B',banda)




