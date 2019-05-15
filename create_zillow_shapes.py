#url = 'http://files.zillowstatic.com/research/public/Zip/Zip_PriceToRentRatio_AllHomes.csv'
import pandas as pd
import geopandas as gpd

import geopandas as gpd
fp = "cb_2016_us_zcta510_500k/cb_2016_us_zcta510_500k.shp"
zip_codes = gpd.read_file(fp)
zip_codes.rename(columns={'ZCTA5CE10':'zip'}, inplace=True)
zip_codes = zip_codes.convert_objects(convert_numeric=True)
print(type(zip_codes))
print('crs=' , zip_codes.crs)
print(zip_codes.head())
print(len(zip_codes))


zillow = pd.read_csv('Zip_PriceToRentRatio_AllHomes.csv', header=0, encoding='ISO-8859-1', low_memory=False)
zillow.rename(columns={'RegionName':'zip'}, inplace=True)
zillow = zillow.convert_objects(convert_numeric=True)
print(zillow.head())
print(list(zillow))
print(len(zillow))


#import matplotlib.pyplot as plt
#plt.figure()
#hist = zillow_shapes['2019-03'].hist(bins=10)
#zillow.hist(column='2019-03', bins=20)
#zillow.plot(kind ='bar')



zillow_shapes = zip_codes.merge(zillow, on='zip')
print(zillow_shapes.head())
print(len(zillow_shapes))

out = r'zillow_shapes.shp'
#zillow_shapes.to_file(out)
