#create shapefile for zip codes
#url = 'http://files.zillowstatic.com/research/public/Zip/Zip_PriceToRentRatio_AllHomes.csv'
import pandas as pd
import geopandas as gpd

import geopandas as gpd
fp = "cb_2016_us_zcta510_500k/cb_2016_us_zcta510_500k.shp"
zip_codes = gpd.read_file(fp)
zip_codes.rename(columns={'ZCTA5CE10':'zip'}, inplace=True)
zip_codes = zip_codes[['zip', 'geometry']]
zip_codes = zip_codes.convert_objects(convert_numeric=True)
print(type(zip_codes))
print('crs=' , zip_codes.crs)
print(zip_codes.head())
print(len(zip_codes))


zillow = pd.read_csv('Zip_PriceToRentRatio_AllHomes.csv', header=0, encoding='ISO-8859-1', low_memory=False)
zillow.rename(columns={'RegionName':'zip'}, inplace=True)
zillow = zillow[['zip', 'City', 'State', 'Metro', 'CountyName', '2019-03']]
zillow = zillow.convert_objects(convert_numeric=True)
print(zillow.head())
print(list(zillow))
print(len(zillow))


#import matplotlib.pyplot as plt
#plt.figure()
#zillow['2019-03'].hist(bins=100)
#plt.show()

pd.options.mode.chained_assignment = None
zillow['range'] = ''
for x in range(0,len(zillow)):
    value = zillow['2019-03'].iloc[x]
    if value < 8:
        zillow['range'].iloc[x] = '1. less than 8 (green)'
    elif 8 < value < 12:
        zillow['range'].iloc[x] = '2. 8-12 (yellow)'
    elif 12 < value < 16:
        zillow['range'].iloc[x] = '3. 12-16 (orange)'
    elif 16 < value < 20:
        zillow['range'].iloc[x] = '4. 16-20 (red)'
    elif value > 20:
        zillow['range'].iloc[x] = '5. greater than 20 (blue)'

zillow_shapes = zip_codes.merge(zillow, on='zip')
print(zillow_shapes.head())
print(list(zillow_shapes))
print(len(zillow_shapes))

out = r'zillow_shapes.shp'
zillow_shapes.to_file(out)
