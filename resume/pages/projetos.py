import dash
from dash import html, dcc, Input, Output, State, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar
import numpy as np
import gc



dash.register_page(__name__, title='Projetos - Data Science', order=1)

header = html.Div([
    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),

    # html.H3('Projetos de aplicações web para visualização de dados'),

    dcc.Markdown(
        '''

        ### Olá, seja bem vindx à minha página de projetos! 👋


        Nessa página apresento alguns projetos de Análise e Visualização de Dados. 
        Tenho me dedicado a transformar os meus projetos em Aplicações Web para facilitar o compartilhamento e 
        apresentação desses projetos. Nesta página apresento alguns deles.

        ----

        '''
        ),
    html.Br(),

dbc.Accordion([

  dbc.AccordionItem([

        dcc.Markdown(
    
            '''
            ----
            A PEDEA é uma plataforma que apresenta dados ambientais diversos a partir de um servidor geográfico. 
            A plataforma foi desenvolvida no âmbito do Programa Cientista Chefe em Meio Ambiente em parceria com a 
            Secretaria do Meio Ambiente do Estado do Ceará. O objetivo do projeto Sig Ambiental é criar um repositório 
            de dados ambientais e disponibilizar estes dados em benefício da sociedade civil e órgãos de gestão do Estado. 
            Para isso, foi adquirido diversos dados georreferenciados que foram processados e disponibilizados na plataforma.
    
            A plataforma foi desenvolvida em React sendo alimentada a partir do Geoserver e banco de dados PostGIS. 
            Minhas atribuições nesse projeto estão relacionadas à aquisição e análise dos dados e auxílio na alimentação
            do banco de dados, bem como a realização de testes automatizados e divulgação da plataforma.
    
            '''
            ,style={'textAlign': 'justify'}),
    
            dbc.Row([
            html.A([

            html.Span('Para acessar a aplicação em tela cheia, clique aqui!!')
            ], href='https://pedea.sema.ce.gov.br/portal/', 
               target="_blank"),
            html.Iframe(
                src="https://pedea.sema.ce.gov.br/portal/",
                style={'align-items': 'center', 'textAlign':'center',"height": "980px", 'border':'1px grey solid','border-radius':10})
            ],justify="center", align="center", className="h-50"),

            html.Br(),
            html.Br(),
    
    ], title = 'Plataforma Estadual de Dados Ambientais (PEDEA) 🌳' ),

    dbc.AccordionItem([
        dcc.Markdown(

                '''
                -----
                O projeto Find My Address surgiu de uma necessidade da minha equipe de trabalho para encontrar as coordenadas
                de um endereço. Podemos encontrar as coordenadas de um dado endereço utilizando a biblioteca 
                [Geopy](https://geopy.readthedocs.io/en/stable/). Trata-se de um trabalho simples de se realizar em sua maquina local,
                como segue no exemplo abaixo:

                ```python


                from geopy.geocoders import Nominatim

                geolocator = Nominatim(user_agent="MyApp")
                location = geolocator.geocode('Cidade Universitaria, São Paulo')

                print(location)

                Out: Location(Cidade Universitária Armando de Salles Oliveira, Avenida Arruda Botelho, Alto de Pinheiros, 
                São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, 
                São Paulo, Região Sudeste, 05466-000, Brasil, (-23.56096405, -46.72770807289966, 0.0))
                ```

                Para uma melhor visualização do processo e para a utilização do algoritmo por colegas que não trabalham com python, desenvolvi 
                a aplicação abaixo para realizar esta consulta:


                '''
                ,style={'textAlign': 'justify'}),

                dbc.Row([
                html.A([

                html.Span('Para acessar a aplicação em tela cheia, clique aqui!!')
                ], href='https://find-my-address.onrender.com/', 
                   target="_blank"),
                html.Iframe(
                src="https://find-my-address.onrender.com/",
                style={'align-items': 'center', 'textAlign':'center',"height": "800px",'border':'1px grey solid','border-radius':10})
                ],justify="center", align="center", className="h-50"),


                html.Br(),
                html.Br(),

        ],title = 'Find My Address 🌎'),

        dbc.AccordionItem([
            dcc.Markdown(
                '''

                ----

                O Banco Nacional de Dados Oceanográficos(BNDO) é uma coletânea de dados oceanográficos admnistrado pela Marinha do Brasil. 
                Os dados do BNDO integram o [Atlas Digital Costeiro e Marinho](https://www.sema.ce.gov.br/89965-2/planejamento-costeiro-e-marinho-do-ceara/atlas-digital-costeiro-e-marinho-do-ceara/)
                que foi publicado no ano de 2021 no âmbito do Programa Cientista Chefe em Meio Ambiente do qual faço parte. 
                Para auxiliar na visualização dos dados, desenvolvi um dashboard para selecionar os dados de interesse e favorecer o download desses dados
                por meio de uma tabela.

                O dashboard foi desenvolvido em python utilizando as bibliotecas [Dash e Plotly](https://dash.plotly.com/) e publicado utilizando o Google Cloud Plataform:

                '''

                ,style={'textAlign': 'justify'}),


            dbc.Row([
            html.A([

            html.Span('Para acessar o dashboard em tela cheia, clique aqui!!')
            ], href='https://dash-bndo.uc.r.appspot.com/', 
               target="_blank"),
            html.Iframe(
            src="https://dash-bndo.uc.r.appspot.com/",
            style={'align-items': 'center', 'textAlign':'center',"height": "800px",'border':'1px grey solid','border-radius':10})
            ],justify="center", align="center", className="h-50"),


        ],title = 'Dashboard BNDO 🌊'),


        dbc.AccordionItem([
            dcc.Markdown(
                '''
                ----

                Projeto de Web Scraping para acessar páginas web fazer a busca de umas string dentro de links dentro desta página.
                O projeto surgiu da necessidade de conferir os links de download de metadados dentro da Plataforma Estadual de Dados 
                Ambientais do Estado do Ceará. O algoritmo realiza uma busca na pagina fornecida e acessa todos os links da classe html 
                fornecida pelo usuário. Para realizar essa tarefa foi utilizado a biblioteca [Selenium](https://selenium-python.readthedocs.io/).

                No exemplo abaixo, é realizado uma busca pela string 'HTTP Status 404', nos links da classe 'MetaLink', no site da plataforma.
                Os links em que a string foi encontrada são apresentados em uma tabela, como mostrado no exemplo abaixo:


                '''

                ,style={'textAlign': 'justify'}),



            dbc.Row([
            html.Img(
            src='assets/web.png',
            style={'align-items': 'center', 'textAlign':'center'}),

            ],justify="center", align="center", className="h-50"),

            html.Br(),

            html.Br(),

            html.Br(),


            dcc.Markdown(
                '''

                O algoritmo para fazer a busca na maquina local é relativamente simples: 


                ```python

                from selenium import webdriver

                string_busca = 'HTTP Status 404'
                driver = webdriver.Chrome()
                #Acessando o site que será realizado a busca
                driver.get("http://pedea.sema.ce.gov.br/portal/")
                #Encontrando os elementos por classe
                elements = driver.find_elements(By.CLASS_NAME, 'MetaLink')
                #Criando lista de endereços com todos os elementos
                metalinks = [element.get_attribute('href') for element in elements]
                #Loop para encontrar as páginas que contém a string de busca
                links = []
                for href in metalinks:
                    driver.get(href)
                    if string_busca in driver.page_source:
                        links.append(href)

                '''

                ),
        ], title = 'Web Search 🔎'),





        # dbc.AccordionItem([
        #     dcc.Markdown(
        #         '''

        #         --------


        #         Projeto de Machine Learning para estimar o potencial de faturamento para os bairros de São Paulo
        #         a partir dos dados de potencial de faturamento dos bairros da cidade do Rio de Janeiro.

        #         Para esse case de Machine Learning, dispomos dos dados de sociodemografia para os bairros do Rio de
        #         Janeiro. A partir desses dados, se pede que seja montado uma análise para os bairros de São Paulo, respondendo
        #         as seguintes questões:

        #         1. Estimar o faturamento que uma loja teria em cada um dos bairros.
        #         2. Classificar o potencial de cada bairro como Alto, Médio ou Baixo.
        #         3. Segmentar os bairros de São Paulo de acordo com a renda e a idade, e indicar 
        #         aqueles com maior aderência ao público alvo.

        #         Consideramos como público alvo desta empresa a população de adultos entre 25 a 50 anos, das classes 
        #         A(rendas A1 e A2) e B(rendas B1 e B2).

        #         Trata-se de um bom case para exercitar técnicas de machine learning, dado que entre as questões levantadas,
        #         é necessário aplicar algoritmos de Regressão, Classificação e Clusterização.

        #         Apresento abaixo uma versão simplificada da resolução do case. Para maiores detalhes acesse o repositorio
        #         do GitHub.


        #         ###### Pré-processamento dos dados

        #        ```python

        #         import pandas as pd 
        #         import numpy as np


        #         # Leitura e pre-processamento do dataset
        #         file = 'DadosDesafioCientista.xlsx'
        #         dataset = pd.read_excel(file,na_values = '-')

        #         ## SimpleImputer para preencher valores NaN
        #         s_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
        #         s_imputer = s_imputer.fit(dataset.iloc[:,4:-2])
        #         dataset.iloc[:,4:-2] = s_imputer.transform(dataset.iloc[:,4:-2])


        #         ```

        #         ###### Aplicação do modelo de regressão *Random Forest Regressor* para estimar o faturamento.

        #        ```python

        #         from sklearn.ensemble import RandomForestRegressor
        #         from sklearn.model_selection import GridSearchCV, train_test_split, KFold

        #         # Tunando hiperparametros utilizando GridSearchCV
        #         # Podemos escolher os parametros que iremos testar, caso optemos por muitos parametros, podemos
        #         # utilizar o RandomizedSearchCV ao invés do GridSearchCV

        #         param_grid_RFR = { 'n_estimators'     : [10,50,100,200,300, 400, 500],
        #                            'criterion'        : ['mse', 'mae'],
        #                            'max_features'     : ['auto', 'sqrt'],
        #                            'max_depth'        : [10, 35, 60, 85, 110],
        #                            'min_samples_split': [2, 5, 10],
        #                            'min_samples_leaf' : [1, 2, 4],
        #                            'bootstrap'        : [True, False]}


        #         # Selecionando os dados dos bairros do Rio de Janeiro para treinar o nosso modelo
        #         df_train = dataset[dataset['estado'] == 'RJ']

        #         # Dividindo o dataset em treino e teste
        #         X_train = df_train.iloc[:,4:-2].values
        #         y_train = df_train.iloc[:,-2].values
        #         X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size = 0.25, random_state = 1)

        #         # Criando modelo para utilizar no GridSearchCV   
        #         rf = RandomForestRegressor(random_state=11)

        #         # Busca de hiperparametros ideais para o nosso modelo
        #         search = GridSearchCV(estimator = rf, param_grid = param_grid, 
        #                                 cv = KFold(n_splits = 5), n_jobs = -1, 
        #                                 verbose = 2, scoring = 'r2')

        #         search.fit(X_train, y_train)


        #         # Treinando o modelo utilizando os melhores hiperparametros encontrados pelo GridSearchCV
        #         RFR = RandomForestRegressor(**search.best_params_, random_state=11)
        #         RFR.fit(X_train,y_train)


        #         # Testando o modelo
        #         y_train_pred = RFR.predict(X_train)
        #         y_test_pred = RFR.predict(X_test)

        #         # Calculando métricas de teste e treino
        #         r2_train = r2_score(y_train, y_train_pred)
        #         r2_test =r2_score(y_test, y_test_pred)

        #         # ------- Métricas -------------
        #         print('R2 Train Score : {:.1%}'.format(r2_train))
        #         print('R2 Test Score : {:.1%}'.format(r2_test))
        #         print('r2 Score Search : {:.1%}'.format(search.best_score_))

        #         ```
        #         ###### Após treinar o nosso modelo de regressão, podemos partir para o algoritmo de Classificação. Os passos que seguiremos serão semelhantes aos apresentados na Regressão, para isso usaremos o *Random Forest Classifier*.

        #        ```python

        #         from sklearn.metrics import accuracy_score 
        #         from sklearn.ensemble import RandomForestClassifier
        #         from sklearn.model_selection import GridSearchCV, train_test_split, KFold


        #         ####### Estimando hiperparametros para a Classificação
        #         param_grid_RFC =  {'n_estimators'     : [50, 100, 200, 300, 400, 500],
        #                            'criterion'        : ["gini", "entropy"],
        #                            'max_depth'        : [10, 35, 60, 85, 110],
        #                            'min_samples_split': [2, 5, 10],
        #                            'min_samples_leaf' : [1, 2, 4],
        #                            'bootstrap'        : [True, False]}


        #         df_train = dataset[dataset['estado'] == 'RJ']

        #         df_train = pd.get_dummies(df_train, columns=['potencial'])

        #         X_train = df_train.iloc[:,4:].values
        #         y_train = df_train.iloc[:, -3::].values

        #         X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size = 0.25, random_state = 1)

        #         RFC = RandomForestClassifier(random_state=11)

        #         search = GridSearchCV(estimator = RFC, param_grid = param_grid_RFC, cv = KFold(n_splits = 5), n_jobs = -1, verbose = 2)
        #         search.fit(X_train, y_train)

        #         RFC = RandomForestClassifier(**search.best_params_,random_state=11)
        #         RFC.fit(X_train,y_train)

        #         y_train_pred = RFC.predict(X_train)
        #         y_test_pred = RFC.predict(X_test)

        #         a_score_train = accuracy_score(y_train, y_train_pred)
        #         a_score_test =accuracy_score(y_test, y_test_pred)


        #         # ------- Métricas -------------
        #         print('Train Accuracy Score : {:.1%}'.format(a_score_train))
        #         print('Test  Accuracy Score : {:.1%}'.format(a_score_test))
        #         print('r2 score search : {:.1%}'.format(search.best_score_))


        #         ```
        #         '''

        #         ,style={'textAlign': 'justify'}),


        #     html.Br(),

        #     dcc.Markdown(
        #         '''

        #         Para apresentar os resultados da Regressão e Classificação, foi criado um Dashboard de acompanhamento
        #         aonde o cliente pode acessar os dados de faturamento e potencial para os bairros do Rio de Janeiro e São Paulo.

        #         '''

        #         ),

        #     dbc.Row([
        #     html.A([

        #     html.Span('Para acessar o dashboard em tela cheia, clique aqui!!')
        #     ], href='https://dash-ml-case1.onrender.com/', 
        #        target="_blank"),
        #     html.Iframe(
        #     src="https://dash-ml-case1.onrender.com/",
        #     style={'align-items': 'center', 'textAlign':'center',"height": "800px",'border':'1px grey solid','border-radius':10}),
        #     html.Br(),
        #     dcc.Markdown('Abaixo temos algumas figuras resultantes do projeto:'),
        #     ],justify="center", align="center", className="h-50"),
        #     dbc.Row([
        #     dbc.Carousel(
        #         items=[
        #             {"key": "1", "src": "assets/ml-figuresw1.png"},
        #             {"key": "2", "src": "assets/ml-figuresw2.png"},
        #             {"key": "3", "src": "assets/ml-figuresw3.png"},
        #             {"key": "4", "src": "assets/ml-figuresw4.png"},
        #             {"key": "5", "src": "assets/ml-figuresw5.png"},
        #             {"key": "6", "src": "assets/ml-figuresw6.png"},
        #         ],
        #         className="carousel-fade",style = {'width':'50%', 'align':'center'},
        #         controls=True,
        #         indicators=False,
        #         interval=2000,
        #         ride="carousel",
        #     ),

        #     ],justify="center", align="center", className="h-50"),




        # ], title = 'Estimativa de faturamento para os bairros de São Paulo - Case Machine Learning 📊'),


        dbc.AccordionItem([
            dcc.Markdown(
                '''
                ----

                Projeto de dashboard utilizando o Google Looker Studio (Data Studio) para acompanhamento de atualização das
                camadas adiconadas à Plataforma Estadual de Dados Espaciais Ambientais (PEDEA) e suas respectivas classes temáticas. 

                '''

                ,style={'textAlign': 'justify'}),

            html.Br(),


            html.A([

                html.Span('Para acessar o dashboard em tela cheia, clique aqui!!')
            ], href='https://datastudio.google.com/embed/reporting/9a718457-19fa-45c0-a14f-41b0a97729b4/page/BLZ7C', 
               target="_blank"),

            dbc.Row([

            html.Iframe(
            src="https://datastudio.google.com/embed/reporting/9a718457-19fa-45c0-a14f-41b0a97729b4/page/BLZ7C",
            style={'align-items': 'center', 'textAlign':'center',"height": "980px",'border':'1px grey solid','border-radius':10}),

            ],justify="center", align="center", className="h-50"),

            html.Br(),

            html.Br(),

            html.Br(),


        ], title = 'Dashboard de acompanhamento PEDEA - GoogleLookerStudio 📑'),






], flush = True, start_collapsed=True)
])

def layout():
    return html.Div([header

        ])