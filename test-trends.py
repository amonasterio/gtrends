import pandas as pd                        
from pytrends.request import TrendReq

pytrends = TrendReq(hl='es-ES', tz=60)
kw_list = ['alba carrillo'] 

# build the payload
pytrends.build_payload(kw_list, timeframe='2020-11-01 2021-11-29', geo='ES')

# store interest over time information in df
df = pytrends.interest_over_time()

print(df[:,0])


'''
pytrends = TrendReq(hl='es-ES')
pytrends.get_historical_interest('forfait grandvalira')
print(pytrends)
'''