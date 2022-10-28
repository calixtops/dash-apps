import plotly.express as px
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import numpy as np 
import dash_bootstrap_components as dbc
import plotly.express as px
from geopy.geocoders import Nominatim
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go

app = Dash(__name__, title="Find My Coordinates", 
            external_stylesheets=[dbc.themes.SLATE],
            meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])


server = app.server


# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',

}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

CARD_TEXT_STYLE2 = {
    'textAlign': 'center',
    'color': '#f55142'
}



df = pd.DataFrame({'Endereço':[],'Latitude':[],'Longitude': []})



controls = dbc.Form(
    [


        html.H4('Digite o endereço que você quer localizar:', 
            style={'textAlign': 'center',
                   'color':'white'
        }),
        html.Br(),


        html.Center(
            [
                dcc.Input(id='adress',
                placeholder='Digite um endereço...',
                ),
                html.P('Ex: Cidade Universitaria, São Paulo'),
    
    
                html.Center([dbc.Button(
                    id='submit_button',
                    n_clicks=0,
                    children='Fazer busca',
                    color='primary',
                ),
                ],style = {'padding-top' : '10%'}),
            ],

            ),



        html.Br(),
        html.Br(),
        html.Hr(),
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.P('Desenvolvedor: '
                                'Pedro Silveira',
                                 style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        

    ],style={'border':'2px #f8f9fa solid',
            'border-radius': 10,
            'padding' : '10%'}
)

sidebar = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        html.Hr(),

        controls
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.Div(id='result',style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=6
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.Div(id='f_adress',style=CARD_TEXT_STYLE2),

                    ]
                ),
            ]

        ),
        md=6
    ),

])



content_second_row = dbc.Row(
    [
    dbc.Col(

        dcc.Loading(dcc.Graph(id='fig',style = {'border':'2px #f8f9fa solid'})),
        md=6
    ),
    dbc.Col(
        dash_table.DataTable(
            id='memory-table',
                style_data={
			'whiteSpace': 'normal',
			'height': 'auto',
			'width': 'auto',
			#'backgroundColor':"#99a89d",
			'color': 'black',
			'weight':'bold'},
		style_header=dict(backgroundColor="black",weight = 'bold'),
        columns=[{'name': i, 'id': i} for i in df.columns]
        ),
        md=6
    ),
    ]
)


content = html.Div(
    [
        html.Div([


                html.Div([
                        html.H2('Aplicação para encontrar coordenadas de um endereço'),

                    ],
                    style = {'padding-top' : '1%',
                            'textAlign': 'center',
                            'color':'white'}
                ),


                ],
                style = {'height' : '30 cm',
                        'border-radius': 10}
                ),  
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        # content_third_row,
        # content_fourth_row
    ],
    style=CONTENT_STYLE
)

app.layout = html.Div([sidebar, content])

@app.callback(
    Output("result", "children"), 
    Output("f_adress", "children"), 
    Output("memory-table", "data"),
    Output("fig", "figure"), 

    [Input('submit_button', 'n_clicks')],
    [State('adress','value')]
    )
def check_adress(n_clicks, adress):

    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(adress)


    if adress == None:

        result = 'Não foi encontrado nada para o endereço: "{}". Tente outra busca'.format(adress)
        f_adress = 'Busque por algum endereço'
        df = pd.DataFrame({'Endereço':[],'Latitude':[],'Longitude': []})
        fig = go.Figure()

    else:


        if location:
            result = 'Encontrando coordenadas para o endereço: {}'.format(adress)
            f_adress = 'Endereço encontrado: {}'.format(location.raw['display_name'])
            f_lat = 'Latitude: {}'.format(location.latitude)
            f_lon = 'Longitude: {}'.format(location.longitude)

            df_dict = {'Endereço':location.raw['display_name'],
                        'Latitude': location.latitude,
                        'Longitude': location.longitude}

            df = pd.DataFrame(df_dict, index = [0])

            df['dummy'] = 1.


            fig = px.scatter_mapbox(df, 
                                    lat="Latitude", lon="Longitude", zoom = 15,
                                    height = 500, size_max=30, size = 'dummy', hover_data = {'Latitude':True,'Longitude':True,'dummy':False},
                                    )



            fig.update_layout(title='Mapa',
                                mapbox_style="open-street-map",
                                margin={"r":5,"t":0,"l":5,"b":0},
                                )

        else:


            result = 'Não foi encontrado nada para o endereço: "{}". Tente fazer outra busca'.format(adress)
            f_adress = 'Busque por algum endereço'
            f_lat = 'Latitude: ------'
            f_lon = 'Longitude: -----'
            df = pd.DataFrame({'Endereço':[],'Latitude':[],'Longitude': []})
            fig = go.Figure()

    return result, f_adress, df.to_dict('records'), fig


if __name__ == '__main__':
    app.run_server(debug = True, port='8085')
