#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.offline as py
import pandas as pd
from plotly import graph_objs as go


# In[2]:


df_aus = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\Australia_2016.csv')
df_canada = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\Canada_2016.csv')
df_india = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\India_2016.csv')
df_ireland = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\Ireland_2016.csv')
df_uk = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\UK_2016.csv')
df_usa = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\USA_2016.csv')
df_frnc = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\FRNC_2016.csv')
df_nry = pd.read_csv('D:\Visualisation\Tableau\TertiaryInternationalStudents\DateWise\NRY_2016.csv')

df_aus=df_aus.fillna(0)
df_canada=df_canada.fillna(0)
df_india=df_india.fillna(0)
df_ireland=df_ireland.fillna(0)
df_uk=df_uk.fillna(0)
df_usa=df_usa.fillna(0)
df_frnc=df_frnc.fillna(0)
df_nry=df_nry.fillna(0)


# In[3]:


csl = [
            [0, '#1E6963'],
            [0.3, '#29B2A7'],
            [0.5, '#29B2A7'],
            [0.7, '#50C6BF'],
            [0.85, '#64E0D8'],
            [1, '#B7FFFE']
        ]

flow_to_aus = go.Choropleth(
        locations = df_aus['CODE'],
        z = df_aus['Value'],
        text = df_aus['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_canada = go.Choropleth(
        locations = df_canada['CODE'],
        z = df_canada['Value'],
        text = df_canada['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_india = go.Choropleth(
        locations = df_india['CODE'],
        z = df_india['Value'],
        text = df_india['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_ireland = go.Choropleth(
        locations = df_ireland['CODE'],
        z = df_ireland['Value'],
        text = df_ireland['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_frnc = go.Choropleth(
        locations = df_frnc['CODE'],
        z = df_frnc['Value'],
        text = df_frnc['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_uk = go.Choropleth(
        locations = df_uk['CODE'],
        z = df_uk['Value'],
        text = df_uk['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )

flow_to_usa = go.Choropleth(
        locations = df_usa['CODE'],
        z = df_usa['Value'],
        text = df_usa['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )
flow_to_nry = go.Choropleth(
        locations = df_nry['CODE'],
        z = df_nry['Value'],
        text = df_nry['COUNTRY'],
        colorscale = csl,
        autocolorscale = False,
        reversescale = True,
        hoverinfo='text+z',
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            thickness = 25,
            tickprefix = '<',
            title = 'Student<br> Count'),
        geo='geo1'
      )


data = [ flow_to_aus, flow_to_canada, flow_to_india, flow_to_ireland, flow_to_frnc,flow_to_uk, flow_to_usa, flow_to_nry]


# In[4]:


## Overall Layout of Visualization e.g. Label, Button, Bar
updatemenus = list([
    dict(active=-1,
         buttons=list([
             dict(label='Australia',
                  method='update',
                  args=[{'visible': [True, False, False,  False, False, False, False, False]}, ]
                  ),
             dict(label='Canada',
                  method='update',
                  args=[{'visible': [False, True, False,  False, False, False, False, False]}, ]
                  ),
             dict(label='India',
                  method='update',
                  args=[{'visible': [False, False, True,  False, False, False, False, False]}, ]
                  ),
            dict(label = 'Ireland',
                 method = 'update',
                 args=[{'visible': [False, False, False, True, False, False, False, False]}, ]
                 ),
            dict(label = 'France',
                 method = 'update',
                 args=[{'visible': [False, False, False, False, True, False, False, False]}, ]
                 ),
            dict(label='United Kingdom',
                  method='update',
                  args=[{'visible': [False, False, False,  False, False, True, False, False]}, ]
                  ),
             dict(label='United States Of America',
                  method='update',
                  args=[{'visible': [False, False, False,  False, False, False, True, False]}, ]
                  ),
             dict(label='Norway',
                  method='update',
                  args=[{'visible': [False, False, False, False, False, False, False, True]}, ]
                  ),
        ]),
         direction = 'up',
         x = 0.1,
         xanchor = 'left',
         y = 0.03,
         yanchor = 'bottom',
        # bgcolor = 'white',
         bordercolor = '#41B3A3',
         font = dict(size=11)
    )
])


# In[5]:


layout = dict(
    title='Global Flow of Tertiary-Level Students<br>\
            Source:<a href="http://data.uis.unesco.org/Index.aspx?queryid=172#">\
            UNESCO(2016)</a>',
    showcoastlines=False,
    geo1=dict(
        showframe=False,
        showcoastlines=False,
        projection=dict(
            type='Mercator'
        ),
     ),
    updatemenus=updatemenus
)
annotations = list([
    dict(text='<b>Select Destination Country</b>', x=0.1, y=0.1, yref='paper', align='left', showarrow=False,font=dict(size=11,)),
])

layout['annotations'] = annotations


# In[6]:


fig = dict( data=data, layout=layout )
py.plot(fig, validate=False, filename='d3-world-map.html')


# In[ ]:




