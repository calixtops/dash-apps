import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Pedro Silveira Calixto', className='mt-3'),
    # dcc.Markdown('### FC Barcelona Forward', className='mb-5'),
    dcc.Markdown('### Informações Pessoais', style={'color':'gray'}),
    dcc.Markdown('Endereço', style=green_text),
    dcc.Markdown('São Paulo, Brasil'),
    dcc.Markdown('Número de Telefone', style=green_text),
    dcc.Markdown('+55 85 996564028'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('calixtops@gmail.com'),
    dcc.Markdown('Linkedin', style=green_text),
    dcc.Markdown('[https://www.linkedin.com/in/calixtops/](https://www.linkedin.com/in/calixtops/)', link_target='_blank'),
    dcc.Markdown('GitHub', style=green_text),
    dcc.Markdown('[https://github.com/calixtops](https://https://github.com/calixtops)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')