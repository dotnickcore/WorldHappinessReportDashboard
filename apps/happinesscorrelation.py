import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pathlib
import numpy as np
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from app import app

# gets relative path
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# loads the datasets
df_2015 = pd.read_csv(DATA_PATH.joinpath("2015.csv"))
df_2016 = pd.read_csv(DATA_PATH.joinpath("2016.csv"))
df_2017 = pd.read_csv(DATA_PATH.joinpath("2017.csv"))
df_2018 = pd.read_csv(DATA_PATH.joinpath("2018.csv"))
df_2019 = pd.read_csv(DATA_PATH.joinpath("2019.csv"))
df_2020 = pd.read_csv(DATA_PATH.joinpath("2020.csv"))

# adding ranks to the 2020 dataset
df_2020['Happiness Rank'] = range(1, len(df_2020.index)+1)

# renaming columns
# 2020
df_2020 = df_2020.rename(columns = {'Country name' : 'Country', 
'Ladder score' : 'Happiness Score', 
'Explained by: Log GDP per capita' : 'Economy (GDP per Capita)', 
'Social support' : 'Family', 
'Healthy life expectancy' : 'Health (Life Expectancy)',
'Freedom to make life choices' : 'Freedom', 
'Perceptions of corruption' : 'Trust (Government Corruption)'})

# 2019
df_2019['Year'] = 2019
df_2019 = df_2019.rename(columns = {'Overall rank':'Happiness Rank', 
'Country or region' : 'Country', 
'Score' : 'Happiness Score',
'GDP per capita' : 'Economy (GDP per Capita)', 
'Social support' : 'Family',
'Healthy life expectancy' : 'Health (Life Expectancy)',
'Freedom to make life choices' : 'Freedom',
'Perceptions of corruption' : 'Trust (Government Corruption)'})

# 2018
df_2018['Year'] = 2018
df_2018 = df_2018.rename(columns = {'Overall rank':'Happiness Rank',
'Country or region' : 'Country',
'Score' : 'Happiness Score',
'GDP per capita' : 'Economy (GDP per Capita)',
'Social support' : 'Family',
'Healthy life expectancy' : 'Health (Life Expectancy)',
'Freedom to make life choices' : 'Freedom',
'Perceptions of corruption' : 'Trust (Government Corruption)'})

# 2017
df_2017['Year'] = 2017
df_2017 = df_2017.rename(columns = {'Happiness.Rank':'Happiness Rank',
'Happiness.Score' : 'Happiness Score', 
'Economy..GDP.per.Capita.' : 'Economy (GDP per Capita)',
'Health..Life.Expectancy.' : 'Health (Life Expectancy)',
'Trust..Government.Corruption.' : 'Trust (Government Corruption)',
'Dystopia.Residual' : 'Dystopia Residual'})

# 2016
df_2016['Year'] = 2016

# 2015
df_2015['Year'] = 2015

# concat all datasets
df_all = pd.concat([df_2020,df_2019,df_2018,df_2017,df_2016,df_2015])
df_all=df_all[['Country', 'Happiness Rank',
'Happiness Score', 'Economy (GDP per Capita)',
'Family', 'Health (Life Expectancy)',
'Freedom','Trust (Government Corruption)',
'Generosity', 'Year']]

years = [2015, 2016, 2017, 2018, 2019, 2020]

layout = html.Div([
    html.Div([
        dbc.Container([
            dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in years],
            value=years[0],
            clearable=False,
        ),
        dcc.Graph(id="correlation-map"),]),
        dbc.Container([
            dbc.Row([
                dbc.Col(html.Li(children="World Happiness Report Dashboard"), className="mb-2")
            ])
        ])
    ]),
])

@app.callback(
    Output("correlation-map", "figure"), 
    [Input("dropdown", "value")])

def update_correlation_map(year):
    if year == 2015:
        corr = df_2015[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')
    elif year == 2016:
        corr = df_2016[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')
    elif year == 2017:
        corr = df_2017[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')
    elif year == 2018:
        corr = df_2018[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')
    elif year == 2019:
        corr = df_2019[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')
    elif year == 2020:
        corr = df_2020[['Happiness Score', 'Economy (GDP per Capita)','Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)','Generosity']].astype(float).corr()
        l = list(corr.columns)

        fig = ff.create_annotated_heatmap(np.array(round(corr,4)), x=l, y=l, colorscale = 'Bluered', reversescale=True )
        fig.update_layout(title='')

    return fig