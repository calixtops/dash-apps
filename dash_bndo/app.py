import plotly.express as px
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import numpy as np 
import gc
import dash_bootstrap_components as dbc
import plotly.express as px


app = Dash(__name__, title="Dados BNDO", external_stylesheets=[dbc.themes.CERULEAN])

server = app.server

range_prof = range(0,3000,10)

cols_temp = ['Data-Hora', 'Longitude [deg]', 'Latitude [deg]', 'Profundidade [m]', 
'Temperatura [°c]','Equipamento', 'Plataforma', 'Comissão','Projeto', 'Mídia']
hv_data_temp = ['Data-Hora', 'Projeto', 'Profundidade [m]','Temperatura [°c]', 'Equipamento']

dtypes={'Data-Hora': str, 'Longitude [deg]': np.float64, 'Latitude [deg]': np.float64, 'Profundidade [m]': np.float64,
'Equipamento': str, 'Plataforma': str, 'Comissão':str ,'Projeto':str , 'Mídia':str}

cols_sal = ['Data-Hora', 'Longitude [deg]', 'Latitude [deg]', 'Profundidade [m]', 
'Salinidade [psu]','Equipamento', 'Plataforma', 'Comissão', 'Projeto', 'Mídia']

hv_data_sal = ['Data-Hora', 'Projeto', 'Profundidade [m]','Salinidade [psu]', 'Equipamento']

cols_dens = ['Data-Hora', 'Longitude [deg]', 'Latitude [deg]', 'Profundidade [m]', 
'Densidade ro [kg/m³]','Equipamento', 'Plataforma', 'Comissão', 'Projeto', 'Mídia']

hv_data_dens = ['Data-Hora', 'Projeto', 'Profundidade [m]','Densidade ro [kg/m³]', 'Equipamento']

cols_cur = ['Data-Hora', 'Longitude [deg]', 'Latitude [deg]', 'Profundidade [m]', 
'Velocidade de corrente [cm/s]','Direção de corrente [graus]','Equipamento', 
'Plataforma', 'Comissão', 'Projeto', 'Mídia']

hv_data_cur = ['Data-Hora', 'Projeto', 'Profundidade [m]','Velocidade de corrente [cm/s]','Direção de corrente [graus]', 'Equipamento']

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}
params = ['Temperatura [°c]','Salinidade [psu]','Densidade ro [kg/m³]', 'Velocidade de corrente [cm/s]']
range_prof = range(0,3000,10)

controls = dbc.Form(
    [

        html.H4('Escolha qual parâmetro você deseja analisar:', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(id='param_drop',
                     options=[{'label':x, 'value':x}
                              for x in params],
                     value=params[0]
                     ),
        html.Br(),


        html.H4('Escolha os intervalos de profundidade:', style={
            'textAlign': 'center'
        }),

        html.Label('Profundidade de Superfície:'),  
        dcc.Dropdown(id='prof_ini',
                     options=[{'label':x, 'value':x}
                              for x in range_prof],
                     value=0
                     ),

        html.Label('Profundidade de Fundo:'),  
        dcc.Dropdown(id='prof_final',
                     options=[{'label':x, 'value':x}
                              for x in range_prof],
                     value=10
                     ),

        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
        ),

        html.Br(),
        html.Br(),
        html.Hr(),
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.P('Desenvolvedor: Pedro Silveira Calixto',
                                 style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        

    ]
)

sidebar = html.Div(
    [
        html.H2('Painel de controle', style=TEXT_STYLE),
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
                        html.P('Para ocultar as comissões que aparecem no mapa, clique no nome do projeto que aparece na legenda da figura.' 
                                ' Para voltar a visualizar no mapa, basta clicar no nome novamente.', style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.P('Para visualizar somente uma comissão, dê dois clicks no nome do projeto.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.P('Explore as informações de cada ponto passando o mouse por cima do ponto.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    ),

])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Loading(dcc.Graph(id='fig',style = {'border':'2px #f8f9fa solid'})), md=12
        ),
    ]
)

content_third_row = dbc.Row([
        html.H4('Para exportar a tabela, clique no botão "export" abaixo:'),

        dash_table.DataTable(
        id='table',
        columns=[],
        data=[],
        column_selectable="multi",

        sort_action='native',
        sort_mode='single',
        filter_action='native',
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender",width='auto'),
        style_cell={'textAlign':'left'},
        export_format='xlsx',
        page_action="native",
        style_table={
        'maxHeight': '600px',
        'overflowY': 'scroll',
        'padding-top' : '1%',

        },
        ),
        ])

content = html.Div(
    [
        html.Div([

                html.Div([], className = 'col-2'), 

                html.Div([
                        html.H2('Avaliação dos dados do Banco Nacional de Dados Oceanográficos'),
                        html.H4('Dashboard com apresentação de todos os dados meteoceanográficos para \n'
                            'a região adjacente ao Estado do Ceará, em função da profundidade e parâmetro.'),

                    ],
                    style = {'padding-top' : '1%'}
                ),


                ],
                style = {'height' : '10%',
                        'background-color' : '#e0e0eb',
                        'border-radius': 10}
                ),  
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        content_third_row,
        # content_fourth_row
    ],
    style=CONTENT_STYLE
)
app.layout = html.Div([sidebar, content])

@app.callback(
    Output("fig", "figure"), 
    Output("table", "data"), 
    Output("table", "columns"),

    [Input('submit_button', 'n_clicks')],
    [State('param_drop','value'), State("prof_ini", "value"), State("prof_final", "value")]
    )

def interactive_graphs(n_clicks, param_drop,prof_ini,prof_final):

    s_cols = []


    if param_drop == 'Temperatura [°c]':
        s_cols = cols_temp
        hv_sel = hv_data_temp
    if param_drop=='Salinidade [psu]':
        s_cols = cols_sal
        hv_sel = hv_data_sal
    if param_drop=='Densidade ro [kg/m³]':
        s_cols = cols_dens
        hv_sel = hv_data_dens
    if param_drop=='Velocidade de corrente [cm/s]':
        s_cols = cols_cur
        hv_sel = hv_data_cur
    file = 'bndo.csv'

    df = pd.read_csv(file, usecols = s_cols, engine = 'python', low_memory = True, dtype = dtypes)

    df = df[df[param_drop].notnull()]
    df = df[df[param_drop] != 'None']

    df = df[s_cols]
    df = df[df != 'None']
    df = df[df.notnull()]
    df = df[(df['Profundidade [m]'] >= prof_ini) & (df['Profundidade [m]'] <= prof_final)]
    df['dummy'] = 1.

    fig = px.scatter_mapbox(df, 
                            lat="Latitude [deg]", lon="Longitude [deg]", 
                            color = 'Projeto', hover_data=hv_sel, zoom = 7, size = 'dummy',
                            height = 700, size_max=7, center = dict(lat=-3.1,lon=-39.3),
                            hover_name="Projeto",
                            color_continuous_scale=px.colors.sequential.Rainbow
                                )

    fig.update_layout(title='Mapa com dados da marinha para o parametro:{} entre as profundidade de {} a {}.'.format(param_drop,prof_ini,prof_final),
                        mapbox_style="open-street-map",
                        margin={"r":5,"t":0,"l":5,"b":0}
                        )
    df = df.drop('dummy', axis =1)
    a = df.to_dict('records')
    b = [{"name": i.title(), "id": i, "deletable": True} for i in df.columns]
    gc.collect()
    return fig, a, b


if __name__ == '__main__':
    app.run_server(debug = True, port='8085')
