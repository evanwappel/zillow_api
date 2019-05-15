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


zillow_shapes = zip_codes.merge(zillow, on='zip')
print(zillow_shapes.head())
print(len(zillow_shapes))

out = r'zillow_shapes.shp'
#selection = df[0:50]
zillow_shapes.to_file(out)
"""
# `country_shapes` is GeoDataFrame with country shapes and iso codes
In [7]: country_shapes.head()
Out[7]:
                                            geometry iso_a3
0  (POLYGON ((180 -16.06713266364245, 180 -16.555...    FJI
1  POLYGON ((33.90371119710453 -0.950000000000000...    TZA
2  POLYGON ((-8.665589565454809 27.65642588959236...    ESH
3  (POLYGON ((-122.84 49.00000000000011, -122.974...    CAN
4  (POLYGON ((-122.84 49.00000000000011, -120 49....    USA

# `country_names` is DataFrame with country names and iso codes
In [8]: country_names.head()
Out[8]:
                       name iso_a3
0                      Fiji    FJI
1                  Tanzania    TZA
2                 W. Sahara    ESH
3                    Canada    CAN
4  United States of America    USA

# Merge with `merge` method on shared variable (iso codes):
In [9]: country_shapes = country_shapes.merge(country_names, on='iso_a3')

In [10]: country_shapes.head()
Out[10]:
                                            geometry iso_a3                      name
0  (POLYGON ((180 -16.06713266364245, 180 -16.555...    FJI                      Fiji
1  POLYGON ((33.90371119710453 -0.950000000000000...    TZA                  Tanzania
2  POLYGON ((-8.665589565454809 27.65642588959236...    ESH                 W. Sahara
3  (POLYGON ((-122.84 49.00000000000011, -122.974...    CAN                    Canada
4  (POLYGON ((-122.84 49.00000000000011, -120 49....    USA  United States of America
"""
