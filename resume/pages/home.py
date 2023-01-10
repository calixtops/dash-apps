import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path = '/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([




    dcc.Markdown('''# Pedro Silveira Calixto''', 
        style={'textAlign':'center','display':'inline'}),


    dcc.Markdown('''[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/calixtops/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/calixtops)''', 
        style={'textAlign':'center','display':'inline'}),


    dcc.Markdown('### Resumo Profissional', style={'textAlign': 'center'}),



    html.Hr(),

    dcc.Markdown(

                '''

                Oceanógrafo com ampla experiência em projetos de apoio à pesquisa e desenvolvimento. 
                Sou mestre em ciências pela Universidade de São Paulo e possuo experiência em análise 
                de dados meteoceanográficos, modelos e dados observacionais. Tive a satisfação de atuar como
                docente pela Universidade Federal do Ceará, aonde lecionei disciplinas relacionadas
                à análise e apresentação de dados oceanográficos e dinâmica de fluidos. Atualmente colaboro 
                com o Programa Cientista Chefe Meio Ambiente (SEMA-CE), onde está sendo desenvolvido a Plataforma 
                Estadual de Dados Ambientais (PEDEA). Possuo facilidade em aprender novas tecnologias e estou 
                continuamente buscando o aperfeiçoamento das minhas habilidades. Experiência na execução de modelos 
                de Machine Learning e manipulação de dados em Python.



                ''',className = 'text-justify', style={'textAlign': 'justify'}),

    dcc.Markdown('### Competências', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Data Science
            * Python
            * Machine Learning
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Pandas / Seaborn / Matplotlib / 
            * Dash / Plotly / Bokeh 
            * QGIS
            ''')
        ], width=3),

        dbc.Col([
            dcc.Markdown('''
            * Matlab
            * SQL
            * R
            ''')
        ], width=3)


    ], justify='center'),

    dcc.Markdown('### Experiência Profissional', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2021 - Presente', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador / Profissional SIG** \n'
                         '*Programa Cientista Chefe Meio Ambiente* \n'
                         '*Secretaria do Meio Ambiente - Fortaleza, Ceará*',
                         style={'white-space': 'pre'},
                         ),


            dcc.Markdown('Projeto financiado pela Fundação Cearense de Apoio ao Desenvolvimento Científico e Tecnológico (FUNCAP). \n'
                        'Visa articular a pesquisa científica com demandas da gestão pública em benefício da sociedade.',
                         ),

            dcc.Markdown(

                '''
            - Elaboração de documento com normas e padrões para a produção e armazenamento de dados georeferenciados e metadados.
            * Aquisição e padronização de dados ambientais de vários pontos focais no Estado.
            * Criação de um banco de dados (PostGIS) e apresentação através da 
            [Plataforma Estadual de Dados Ambientais](https://pedea.sema.ce.gov.br/portal/).
            * Ferramentas utilizadas: QGIS / Python / Dash / SQL


                '''


                ),

        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2021 - 06/2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**CEO** \n'
                         '*SIARA Tecnologia e Consultoria Ambiental*',
                         style={'white-space': 'pre'},
                         ),
            dcc.Markdown('''Constituição de uma start-up de tecnologia ambiental, promovido pelo Programa \
                [Clusters Econômicos de Inovação](https://www.sedet.ce.gov.br/clusters-e-i-2/).''',
                ),

            dcc.Markdown(

                '''

                * Projeto relacionado à energia eólica e a falta de soluções preditivas para programar a manutenção periódica dos equipamentos.
                * Desenvolvimento de uma aplicação em Flutter alimentada por uma API meteorológica e análise usando inteligência artificial 
                para ajudar a planejar a manutenção obrigatória de equipamentos.
                * Ferramentas utilizadas: Flutter / Python
                '''

                )




        ], width=5)
    ], justify='center'),



        dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2019 - 03/2021', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Professor Substituto da Carreira do Magistério Superior** \n'
                         '*Instituto de Ciências do Mar, Universidade Federal do Ceará* \n',
                         style={'white-space': 'pre'},
                         ),


            dcc.Markdown('Componentes curriculares ministradas para os cursos de graduação em Oceanografia e Ciências Ambientais:',
                          ),

            dcc.Markdown(

                '''
                * Análise e Apresentação de Dados Oceanográficos em Python
                * Interação Oceano-Atmosfera.
                * Oceanografia Física Descritiva 
                * Oceanografia Dinâmica I

                '''

                )

        
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('02/2017 - 02/2019',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador** \n'
                         '*Fundação Cearense de Meteorologia e Recursos hídricos (FUNCEME)*',
                         style={'white-space': 'pre'},
                         ),
            dcc.Markdown('Assistência técnica e científica em projetos de pesquisa e desenvolvimento relacionados \n'
                         'ao tempo e clima, com foco nos recursos hídricos do Estado do Ceará.',
                         ),

            html.Ul([
                html.Li(
                    'Aquisição, processamento e apresentação de dados meteorológicos e oceanográficos.'),
                html.Li(
                    'Ferramentas utilizadas: Python (Seaborn, Matplotlib, Pandas, ggplot2) / Matlab / Fortran'),
            ])
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('2015 - 2016',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Pesquisador Colaborador** \n'
                         '*Petróleo Brasileiro S.A - Petrobras*',
                         style={'white-space': 'pre'},
                         ),
            dcc.Markdown('Utilização de dados observacionais e modelos para a caracterização física da \n'
                        'plataforma continental e região oceânica proxima aos estados do Espirito Santo e \n'
                        'Sergipe-Alagoas, Brasil.',
                         ),

            html.Ul([
                html.Li(
                    'Caracterização da Circulação e das Massas de Água na Bacia do Espírito Santo- AMBES'),
                html.Li(
                    'Caracterização da Circulação e das Massas de Água na Bacia Sergipe-Alagoas - SEAL'),
            ])
        ], width=5)
    ], justify='center'),


    dcc.Markdown('### Educação', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2016',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Mestrado em Ciência**s\n'
                         '*Universidade de São Paulo - São Paulo, SP*',
                         style={'white-space': 'pre'},
                         ),
        ], width=5)
    ], justify='center'),


    dbc.Row([
        dbc.Col([
            dcc.Markdown('2014',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Graduação em Oceanografia** \n'
                         '*Universidade Federal do Ceará - Fortaleza, CE*',
                         style={'white-space': 'pre'},
                         ),
        ], width=5)
    ], justify='center'),


    dcc.Markdown('### Cursos', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 

                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(

                        '![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white) \n'


                        '**Machine Learning A-Z™: Hands-On Python & R In Data Science** \n'
                        '[Credential ID UC-14cd6c98-1044-4cb2-891d-32f72d442a58](https://www.udemy.com/certificate/UC-14cd6c98-1044-4cb2-891d-32f72d442a58/)',
                        style={'white-space': 'pre'}
                        ),
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 


                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(


                        '![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white) \n'


                        '**Looker Studio (Google Data Studio)** \n'
                        '[Credential ID UC-84cbb1e6-cae0-44b4-bc53-8959d5fc560f](https://www.udemy.com/certificate/UC-84cbb1e6-cae0-44b4-bc53-8959d5fc560f/)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),

        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Machine Learning: classificação com SKLearn** \n'
                        '[Credential ID bf57632f-1780-4952-95fc-1d1c103e88b9](https://cursos.alura.com.br/certificate/bf57632f-1780-4952-95fc-1d1c103e88b9)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),




    dbc.Row([
        dbc.Col([
            dcc.Markdown('''

                        2022 



                        ''',
                         style={'textAlign': 'center'}),
        ], width=2),


        dbc.Col([
            
            dcc.Markdown(
                        '![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI3NS41MiIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDc1LjUyIDM1Ij48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIwIiB5PSIwIiB3aWR0aD0iNzUuNTIiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDFFNDUiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI3NS41MiIgeT0iMCIgd2lkdGg9IjAiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuMDAgMjJMMTMuNDYgMjJMMTYuNjggMTMuNDdMMTguMDEgMTMuNDdMMjEuMjQgMjJMMTkuNjkgMjJMMTguOTkgMjAuMDFMMTUuNjkgMjAuMDFMMTUuMDAgMjJaTTE3LjM0IDE1LjI4TDE2LjEwIDE4LjgyTDE4LjU4IDE4LjgyTDE3LjM0IDE1LjI4Wk0zMC41NSAyMkwyNS4xOSAyMkwyNS4xOSAxMy40N0wyNi42NyAxMy40N0wyNi42NyAyMC44MkwzMC41NSAyMC44MkwzMC41NSAyMlpNMzQuNTQgMTkuMTZMMzQuNTQgMTkuMTZMMzQuNTQgMTMuNDdMMzYuMDEgMTMuNDdMMzYuMDEgMTkuMThRMzYuMDEgMjAuMDMgMzYuNDUgMjAuNDhRMzYuODggMjAuOTMgMzcuNzMgMjAuOTNMMzcuNzMgMjAuOTNRMzkuNDQgMjAuOTMgMzkuNDQgMTkuMTNMMzkuNDQgMTkuMTNMMzkuNDQgMTMuNDdMNDAuOTEgMTMuNDdMNDAuOTEgMTkuMTdRNDAuOTEgMjAuNTMgNDAuMDQgMjEuMzJRMzkuMTcgMjIuMTIgMzcuNzMgMjIuMTJMMzcuNzMgMjIuMTJRMzYuMjYgMjIuMTIgMzUuNDAgMjEuMzNRMzQuNTQgMjAuNTUgMzQuNTQgMTkuMTZaTTQ2Ljk3IDIyTDQ1LjQ4IDIyTDQ1LjQ4IDEzLjQ3TDQ4LjQ4IDEzLjQ3UTQ5Ljk2IDEzLjQ3IDUwLjc2IDE0LjEzUTUxLjU2IDE0Ljc5IDUxLjU2IDE2LjA1TDUxLjU2IDE2LjA1UTUxLjU2IDE2LjkwIDUxLjE1IDE3LjQ4UTUwLjc0IDE4LjA2IDUwLjAwIDE4LjM3TDUwLjAwIDE4LjM3TDUxLjkyIDIxLjkyTDUxLjkyIDIyTDUwLjMzIDIyTDQ4LjYyIDE4LjcxTDQ2Ljk3IDE4LjcxTDQ2Ljk3IDIyWk00Ni45NyAxNC42Nkw0Ni45NyAxNy41Mkw0OC40OSAxNy41MlE0OS4yNCAxNy41MiA0OS42NiAxNy4xNVE1MC4wOCAxNi43NyA1MC4wOCAxNi4xMUw1MC4wOCAxNi4xMVE1MC4wOCAxNS40MyA0OS42OSAxNS4wNVE0OS4zMCAxNC42OCA0OC41MyAxNC42Nkw0OC41MyAxNC42Nkw0Ni45NyAxNC42NlpNNTYuNzQgMjJMNTUuMjAgMjJMNTguNDIgMTMuNDdMNTkuNzUgMTMuNDdMNjIuOTggMjJMNjEuNDMgMjJMNjAuNzMgMjAuMDFMNTcuNDMgMjAuMDFMNTYuNzQgMjJaTTU5LjA4IDE1LjI4TDU3Ljg1IDE4LjgyTDYwLjMyIDE4LjgyTDU5LjA4IDE1LjI4WiIgZmlsbD0iI0ZGRkZGRiIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9IiIgZmlsbD0iI0ZGRkZGRiIgeD0iODguNTIiLz48L3N2Zz4=) \n'
                        

                        '**Python Pandas: técnicas avançadas** \n'
                        '[Credential ID bf57632f-1780-4952-95fc-1d1c103e88b9](https://cursos.alura.com.br/certificate/4d6ffa65-6e39-47e5-9caf-538ffad253d7)'

                        ,style={'white-space': 'pre'}),
        ], width=5)
    ], justify='center'),



    # dbc.Row([
    #     dbc.Col([
    #         dcc.Markdown('2022',
    #                      style={'textAlign': 'center'}),
    #     ], width=2),

    #     dbc.Col([
            
    #         dcc.Markdown('''
    #                     ![Generic badge](https://img.shields.io/badge/Alura-blue.svg)

    #                     '''),
    #     ], width=5)
    # ], justify='center'),




], className = 'col-sd-4')
