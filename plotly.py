"""
# apt install libatlas-base-dev
# pip3 install plotly 
# pip3 install cufflinks 
  sign up plot.ly and generate API key
  setup user on this machine
# python3
>> import plotly
>> plotly.tools.set_credentials_file(username='**', api_key='**') 
"""

import pandas as pd
import cufflinks as cf
import plotly as py
from plotly import graph_objs as go

"""
  data processing and output dataframes with pandas and cufflinks
"""

cf.go_offline()

# Scatter properties
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html
# this exsample sets two line graphs on the same time axis.
trace1 = go.Scatter(
  name='Graph1',
  x=df['Date'],
  y=df['data1'],
  line=dict(color='green')
)
trace2 = go.Scatter(
  name='Graph2',
  x=df['Date'],
  y=df['data2'],
  line=dict(color='orange'),
  yaxis='y2'
)

data = [trace1, trace2]

# Layout properties
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html
# In thie example, the left and right ticks on this graph are different.
data1min = 5000
data1max = 10000
data2min = 0
data2max = 100
layout = go.Layout(
  template='plotly_white',
  yaxis=dict(range=[data1min,data1max]),
  yaxis2=dict(range=[data2min,data2max], overlaying='y', side='right'),
)

fig = go.Figure(data=data, layout=layout)

# put plotly.min.js and .html in same directory
# https://github.com/plotly/plotly.js/tree/master/dist
# include_plotlyjs=True creates very large HTML file
py.offline.plot(fig, filename='foo.html', include_plotlyjs='./plotly.min.js')
