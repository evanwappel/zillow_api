# Example of how to use pyzillow
# Store your Zillow APY key in a file called
# zillow_api_key.py
from zillow_api_key import zillow_api_key

# Hard code the address
address = '2114 Bigelow Ave'
zip_code = 'Seattle, WA'

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
zillow_data = ZillowWrapper(zillow_api_key)
deep_search_response = zillow_data.get_deep_search_results(address, zip_code)
result = GetDeepSearchResults(deep_search_response)
#result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails

zestimate_amount = result.zestimate_amount
zestimate_last_updated = result.zestimate_last_updated
zestimate_value_change = result.zestimate_value_change
zestimate_valuation_range_high = result.zestimate_valuation_range_high
zestimate_valuationRange_low = result.zestimate_valuationRange_low
zestimate_percentile = result.zestimate_percentile

print "zestimate_amount = ", zestimate_amount
print "zestimate_last_updated = ", zestimate_last_updated
print "zestimate_value_change = ", zestimate_value_change
print "zestimate_valuation_range_high = ", zestimate_valuation_range_high
print "zestimate_valuationRange_low = ", zestimate_valuationRange_low
print "zestimate_percentile = ", zestimate_percentile



# from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails
# zillow_id = result.zillow_id
# zillow_data = ZillowWrapper('X1-ZWz1b7i64mghzf_ako3m')
# updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
# result = GetUpdatedPropertyDetails(updated_property_details_response)
# result.rooms # number of rooms of the home