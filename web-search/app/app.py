import pandas as pd
from dash import Dash, dash_table, dcc, html, Input, Output, State
import numpy as np 
import dash_bootstrap_components as dbc
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary

app = Dash(__name__, title="Web Search", 
            external_stylesheets=[dbc.themes.QUARTZ],
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
}





df = pd.DataFrame({'Links em que a busca foi encontrada':[]})



controls = dbc.Form(
    [


        html.H4('Digite o endereço que você quer localizar:', 
            style={'textAlign': 'center',
                   'color':'white'
        }),
        html.Br(),

        html.P('Digite o endereço do site:'),
        
        dcc.Input(id='site',
        placeholder='Endereço web',
        ),

        html.P('ex: http://pedea.sema.ce.gov.br/portal/',style = {'padding-top': '-15px'}),



        html.P('Em qual classe está o link?'),
    
        dcc.Input(id='link',
        placeholder='ClassName',
        ),
        html.P('ex: MetaLink',style = {'padding-top': '-15px'}),


        html.P('Qual palavra buscar?'),
        dcc.Input(id='search',
        placeholder='Busca',
        ),
        html.P('ex: HTTP Status 404',style = {'padding-top': '-15px'}),


        html.Center([
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Fazer busca',
            color='primary',
        ),
        ],style = {'padding-top' : '10%'}),

        html.Br(),
        html.Br(),
        html.Hr(),
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        dcc.Markdown('Desenvolvedor:'),
                        dcc.Markdown('Pedro Silveira Calixto'),
                    ]
                ,style=CARD_TEXT_STYLE),
            ]
        ),
        

    ],style={'border':'2px #f8f9fa solid',
            'border-radius': 10,
            'padding' : '10%'}
)

sidebar = html.Div(
    [

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
                        html.Div(id='msg1',style=CARD_TEXT_STYLE),
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
                        html.Div(id='msg2',style=CARD_TEXT_STYLE),

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
        dash_table.DataTable(
            id='memory-table',
                style_data={
			'whiteSpace': 'normal',
			'height': 'auto',
			'width': 'auto',
			#'backgroundColor':"#99a89d",
			'color': 'black',
			'weight':'bold'},
        column_selectable="multi",
        export_format='xlsx',
        page_action="native",
		style_header=dict(backgroundColor="black"),
        columns=[{'name': i, 'id': i} for i in df.columns]
        ),
        md=12
    ),
    ]
)


content = html.Div(
    [
        html.Div([


                html.Div([
                        html.H2('WebSearch - Encontre uma string dentro de links de um site'),

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
    Output("msg1", "children"), 
    Output("msg2", "children"), 
    Output("memory-table", "data"),

    [Input('submit_button', 'n_clicks')],
    [State('site', 'value'),
     State('link' , 'value'),
     State('search' , 'value')]
    )
def check_adress(n_clicks, site, link, search):

    try:

        if n_clicks>0:

            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(chrome_options=options)

            driver.get(str(site))

            elements = driver.find_elements(By.CLASS_NAME, str(link))

            metalinks = [element.get_attribute('href') for element in elements]

            error = []

            for href in metalinks:
                driver.get(href)
                if str(search) in driver.page_source:
                    error.append(href)

            df = pd.DataFrame({'Links em que a busca foi encontrada':error})

            msg1 = 'Fazendo busca no endereço web: {}!'.format(site)
            msg2 = 'Foram encontradas {} ocorrências para a string buscada!'.format(len(error))

        else: 

            df = pd.DataFrame({'Links em que a busca foi encontrada':[]})
            msg1 = 'Faça uma busca!'
            msg2 = 'Tenha certeza da classe que abriga o link que você busca!'

    except:

        df = pd.DataFrame({'Links em que a busca foi encontrada':[]})
        msg1 = 'Não foi encontrado nada para essa busca!'
        msg2 = 'Pode ser ruim ou pode ser bom!'

    return msg1,msg2,df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug = True, port='8085')
