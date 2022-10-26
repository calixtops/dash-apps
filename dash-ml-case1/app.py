#!/usr/bin/env python3

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, title="Dashboard Geofusion", external_stylesheets=external_stylesheets)

server = app.server

df = pd.read_csv('DadosDesafioCientista_full.csv')

mensagem = 'Para exportar a tabela, clique no botão "export" abaixo:'
msg_plot = 'Utilize o slider para escolher o número de bairros a incluir no gráfico.'

app.layout = html.Div([
    html.Div([

            html.Div([], className = 'col-2'), 

            html.Div([
                html.H1(children='  Faturamento e Potencial para os bairros do Rio de Janeiro e São Paulo',
                        style = {'textAlign' : 'center',
                                 'color': 'grey'}
                )],
                className='col-8',
                style = {'padding-top' : '1%'}
            ),


            ],
            className = 'row',
            style = {'height' : '3%',
                    'background-color' : '#d3dbfe'}
            ),

    html.P('Escolha qual cidade você deseja analisar:'),
    dcc.Dropdown(id='city-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.cidade.unique())],
                 value='São Paulo'
                 ),

    html.Div([


        html.Hr(style={
        'margin-top':'-2px',
        'height':'7px',
        'background-color':'#00cc00',
        'border':'none',
        }),
        html.P(mensagem),   

    html.Div([
        dash_table.DataTable(
        id='table',
        columns=[{"name": i.title(), "id": i, "deletable": True} 
                 for i in df.columns],
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
    ]),

        html.Br(),
        html.Hr(),
        html.H3(msg_plot),
        dcc.Slider(
            id="bairros",
            min=1,
            max=df.shape[0],
            value=df.shape[0],
            ),

        dcc.Graph(id='fig')
    ]),
    
])


# -----------------------------------------Callback--------------------------------------------

@app.callback(
    Output("fig", "figure"), 
    Output("table", "data"), 
    Output("bairros", "max"),

    Input('city-choice','value'),
    Input("bairros", "value"),
    )

def interactive_graphs(value_city,bairros):

    df = pd.read_csv('DadosDesafioCientista_full.csv')

    df = df[df.cidade==value_city]

    df_top = df.sort_values('faturamento',ascending= False).head(bairros)

    fig = px.bar(df_top,
    x='nome',
    y='faturamento',
    color='potencial',
    template='ggplot2',
    hover_data=df_top.columns,
    height=600,
    labels=dict(
        nome="Bairros", 
        faturamento="Faturamento", 
        potencial="Potencial",
        height=500),
    color_discrete_map={
    'Alto': '#8080ff',
    'Médio': '#66ff66',
    'Baixo': '#ff8080'},
    title='Faturamento dos bairos de {}.'.format(value_city))

    return fig, df.to_dict('records'), df.shape[0]


if __name__ == '__main__':
    app.run_server(debug=True)
