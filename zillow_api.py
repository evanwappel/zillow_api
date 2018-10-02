# Example of how to use pyzillow
# Store your Zillow APY key in a file called
# zillow_api_key.py
#from zillow_api_key import zillow_api_key

# api_key import
import os
home_dir =  os.path.expanduser('~')
directory_path = home_dir + "/api_keys/"
f = open(directory_path + 'zillow_api', 'r')
API_KEY = f.read().rstrip()
f.close()

# Hard code the address
address = '4271 Fitzwilliam St'
zip_code = 'Dublin, CA'

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
zillow_data = ZillowWrapper(API_KEY)
deep_search_response = zillow_data.get_deep_search_results(address, zip_code)
result = GetDeepSearchResults(deep_search_response)
#, zillow_id # zillow id, needed for the GetUpdatedPropertyDetails


zillow_id = result.zillow_id
home_type = result.home_type
home_detail_link = result.home_detail_link
graph_data_link = result.graph_data_link
map_this_home_link = result.map_this_home_link
latitude = result.latitude
longitude = result.longitude
# coordinates (as GEOS point)
tax_year = result.tax_year
tax_value = result.tax_value
year_built = result.year_built
property_size = result.property_size
home_size = result.home_size
bathrooms = result.bathrooms
bedrooms = result.bedrooms
last_sold_date = result.last_sold_date
last_sold_price_currency = result.last_sold_price_currency
last_sold_price = result.last_sold_price
zestimate_amount = result.zestimate_amount
zestimate_last_updated = result.zestimate_last_updated
zestimate_value_change = result.zestimate_value_change
zestimate_valuation_range_high = result.zestimate_valuation_range_high
zestimate_valuationRange_low = result.zestimate_valuationRange_low
zestimate_percentile = result.zestimate_percentile

print("zillow_id = ", zillow_id)
print("home_type = ", home_type)
print("home_detail_link = ", home_detail_link)
print("graph_data_link = ", graph_data_link)
print("map_this_home_link = ", map_this_home_link)
print("latitude = ", latitude)
print("longitude = ", longitude)
print("tax_year = ", tax_year)
print("tax_value = ", tax_value)
print("year_built = ", year_built)
print("property_size = ", property_size)
print("home_size = ", home_size)
print("bathrooms = ", bathrooms)
print("bedrooms = ", bedrooms)
print("last_sold_date = ", last_sold_date)
print("last_sold_price_currency = ", last_sold_price_currency)
print("last_sold_price = ", last_sold_price)
print("zestimate_amount = ", zestimate_amount)
print("zestimate_last_updated = ", zestimate_last_updated)
print("zestimate_value_change = ", zestimate_value_change)
print("zestimate_valuation_range_high = ", zestimate_valuation_range_high)
print("zestimate_valuationRange_low = ", zestimate_valuationRange_low)
print("zestimate_percentile = ", zestimate_percentile)



# from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails
# zillow_id = , zillow_id
# zillow_data = ZillowWrapper('X1-ZWz1b7i64mghzf_ako3m')
# updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
# result = GetUpdatedPropertyDetails(updated_property_details_response)
# , rooms # number of rooms of the home
