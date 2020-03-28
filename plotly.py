"""
# apt install libatlas-base-dev
# pip3 install pandas 
# pip3 install plotly 
# pip3 install cufflinks 
  sign up plot.ly and generate API key
  setup user on this machine
# python3
>> import plotly
>> plotly.tools.set_credentials_file(username='**', api_key='**') 


Scatter properties
https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html

Layout properties
https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html
"""


import plotly as py
from plotly import graph_objs as go

trace1 = go.Scatter(
  ...,
  ...
)
trace2 = go.Scatter(
  ...,
  ...
)

data = [trace1, trace2]

layout = go.Layout(
  ...,
  ...
)

fig = go.Figure(data=data, layout=layout)
