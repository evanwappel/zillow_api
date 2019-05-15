#url = 'http://files.zillowstatic.com/research/public/Metro/Metro_PriceToRentRatio_AllHomes.csv'

url = 'http://files.zillowstatic.com/research/public/Zip/Zip_PriceToRentRatio_AllHomes.csv'
import pandas as pd
import io
import requests
#url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('ISO-8859-1')))
print(df.head)
