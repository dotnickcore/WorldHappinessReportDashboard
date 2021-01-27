import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

# connects to app.py
from app import app
from app import server

# connect to your app pages
from apps import mosthappiest, leasthappiest, happinessgdpplot, happinesshealthyplot, happinesssocialplot, happinessgenerosityplot, happinessfreedomplot, happinesstrustplot, happinesscorrelation, worldmap
# sets the layout of the page
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    # written introduction of the website and explaining the purpose of the website.
    html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1(children="World Happiness Report Dashboard"), className="mb-2")
            ]),

            dbc.Row([
                dbc.Col(html.P(children="Welcome to the World Happiness Report Dashboard. The The World Happiness Report is a publication of the Sustainable Development Solutions Network, powered by data from the Gallup World Poll. The report is a landmark survey of the state of global happiness that ranks 156 countries by how happy their citizens perceive themselves to be. The data used is from the survey results from 2015 to 2020. The variables for each survey is GDP per capita, life expectancy, social support, freedom to make choices, generosity, and perceptions of corruption."), className="mb-2")
            ]),

            dbc.Row([
                dbc.Col(html.P(children="This online dashboard takes away the industrious process of users analysing surveys to create statistics and assists the user in analysing the surveys with computer code and display graphs. Think of it as your own virtual assistant for analysing datasets and producing statistics."), className="mb-2")
            ])
        ])
    ]),

    # links for the website
    html.Div([
        dbc.Container([
            dbc.Row([
            dbc.Col(dcc.Link('Most Happiest', href='/apps/mosthappiest'), className="mb-2"),
            dbc.Col(dcc.Link('Least Happiest', href='/apps/leasthappiest'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs GDP', href='/apps/happinessgdpplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs Social Services', href='/apps/happinesssocialplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs Life Expectancy', href='/apps/happinesshealthyplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs Generosity', href='/apps/happinessgenerosityplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs Freedom', href='/apps/happinessfreedomplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness vs Trust', href='/apps/happinesstrustplot'), className="mb-2"),
            dbc.Col(dcc.Link('Happiness Correlation', href='/apps/happinesscorrelation'), className="mb-2"),
            dbc.Col(dcc.Link('Interactive World Map', href='/apps/worldmap'), className="mb-2")], className="row"), html.Div(id='page-content', children=[]),
        ])
    ]),
])

# calls the url.
@app.callback(Output('page-content', 'children'), 
              [Input('url', 'pathname')])

# the function will return app pages.
def display_page(pathname):
    if pathname == '/apps/mosthappiest':
        return mosthappiest.layout
    if pathname == '/apps/leasthappiest':
        return leasthappiest.layout 
    if pathname == '/apps/happinessgdpplot':
        return happinessgdpplot.layout
    if pathname == '/apps/happinesshealthyplot':
        return happinesshealthyplot.layout
    if pathname == '/apps/happinesssocialplot':
        return happinesssocialplot.layout
    if pathname == '/apps/happinessgenerosityplot':
        return happinessgenerosityplot.layout
    if pathname == '/apps/happinessfreedomplot':
        return happinessfreedomplot.layout
    if pathname == '/apps/happinesstrustplot':
        return happinesstrustplot.layout
    if pathname == '/apps/happinesscorrelation':
        return happinesscorrelation.layout
    if pathname == '/apps/worldmap':
        return worldmap.layout
    else:
        return mosthappiest.layout

if __name__ == "__main__":
    app.run_server(debug=True)