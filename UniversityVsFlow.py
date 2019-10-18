#!/usr/bin/env python
# coding: utf-8

# In[2]:


import plotly.offline as py
import plotly.graph_objs as go
from plotly import tools
import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv("D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\Country_University_Flow.csv",header =0)

y_saving = df['University']
y_net_worth=df['Student Flow']
x_saving = df['Country']
x_net_worth = df['Country']


# In[4]:


trace0 = go.Bar(
    x=y_saving,
    y=x_saving,
    marker=dict(
        color='rgba(41,178,167, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Home to universities among top 500',
    orientation='h',
)
trace1 = go.Scatter(
    x=y_net_worth,
    y=x_net_worth,
    mode='lines+markers',
    line=dict(
        color='rgb(128, 0, 128)'),
    name='Home to international student population',
)


# In[5]:


layout = dict(
    title='University host countries & global flow of student',
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='bottom',
        dtick=25000,
    ),
    legend=dict(
        x=0.029,
        y=1.038,
        font=dict(
            size=11,
        ),
    ),
    margin=dict(
        l=130,
        r=20,
        t=70,
        b=70,
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
)


# In[6]:


annotations = []

y_s = np.round(y_saving, decimals=2)
y_nw = np.rint(y_net_worth)

# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x_saving):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn- 70000,
                            text='{:,}'.format(ydn) + 'K',
                            font=dict(family='Arial', size=12,
                                      color='rgb(128, 0, 128)'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 4,
                            text=str(yd),
                            font=dict(family='Arial', size=12,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper',
                        #x=-0.2, y=-0.109,
                        x=-0.1, y=-0.109,
                        text='CA682 Data Visualisation Assignment, ' +
                             'Created by Ashish(2016 UNESCO Report)',
                        font=dict(family='Arial', size=10,
                                  color='rgb(150,150,150)'),
                        showarrow=False))

layout['annotations'] = annotations


# In[7]:


# Creating two subplots
fig = tools.make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                          shared_yaxes=False, vertical_spacing=0.001)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)


# In[8]:


fig['layout'].update(layout)
py.plot(fig, filename='University_Global_Student.html')

