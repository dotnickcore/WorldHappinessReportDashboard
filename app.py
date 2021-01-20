import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

# this will set your layout to an external spreadsheet
external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# loads the datasets
df_2015 = pd.read_csv("./datasets/2015.csv")
df_2016 = pd.read_csv("./datasets/2016.csv")
df_2017 = pd.read_csv("./datasets/2017.csv")
df_2018 = pd.read_csv("./datasets/2018.csv")
df_2019 = pd.read_csv("./datasets/2019.csv")
df_2020 = pd.read_csv("./datasets/2020.csv")

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

# sets the layout of the page
app.layout = html.Div(
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children="World Happiness Report Dashboard"), className="mb-2")
        ])
    ]) 
)

if __name__ == "__main__":
    app.run_server(debug=True)