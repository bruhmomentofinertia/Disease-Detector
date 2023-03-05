#installing pytrends
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})
#building payload
kw_list = ["machine learning"] # list of keywords to get data 
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

#interest over time.  essentially shows historical trends

data = pytrends.interest_over_time() 
data = data.reset_index() 


import plotly.express as px

fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
fig.show() 