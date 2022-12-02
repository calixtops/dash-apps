from dash.dependencies import Input, Output, State
from dash import Dash, dash_table, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import geopandas as gpd
import pandas as pd
import dash_uploader as du
from zipfile import ZipFile
from glob import glob
import os
import shutil
from geopy.geocoders import Nominatim
import geocoder


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

server = app.server



def geocod_add(geo_df):

    geolocator = Nominatim(user_agent="MyApp")

    geocod = pd.read_table('geocod_ibge.csv', sep=';')

    a = []
    b = []
    for index, row in geo_df.iterrows(): 
        if geo_df.type[0] == 'Point':
            lat,lon = row.geometry.y,row.geometry.x
        else:
            lat,lon = row.geometry.centroid.y,row.geometry.centroid.x
        coordinates = lat,lon
        city = geocoder.osm(coordinates, method='reverse').town
        
        lat_busca = lat

        while city == None:
            lat_busca = lat_busca - 0.01
            location = geolocator.reverse([lat_busca,lon])

            if location == None:
                city = geocoder.osm([lat_busca,lon], method='reverse').town
            else:
                address = location.raw['address']
                city = address.get('city')


            if city == None:
                city = address.get('town')
                if city == None:
                    city = geocoder.osm([lat_busca,lon], method='reverse').town
                    if city == None:

                        city = address.get('village')

        a.append(city)
        if city == None:
            b.append(99999)
        else:
            try:
                geocod_aprox = geocod[geocod['municipio2'] == city].geocodigo.values[0]
                b.append(geocod_aprox)
            except:
                b.append(99999)
    geo_df['municipio'] = a

    geo_df['geocodigo'] = b


    return geo_df

# path = Path("/projects")
# path.mkdir(parents=True, exist_ok=True)
UPLOAD_FOLDER = r"data/"
du.configure_upload(app, UPLOAD_FOLDER)


app.layout = html.Div(
    [
        html.H1('Adicionar geocodigo e municipio ao shapefile'),
        html.Div(
            du.Upload(
                text='Drag and Drop files here',
                pause_button=False,
                cancel_button=True,
                filetypes=['zip', 'rar'],
                id='upload-files-div',
            ),
            style={
                'textAlign': 'center',
                'width': '600px',
                'padding': '10px',
                'display': 'inline-block'
            },
        ),
        html.Br(),
        dcc.Loading(html.Div(id = 'mensagem')),



        dbc.Button(id='btn',
            children=[html.I(className="fa fa-download mr-1"), "Iniciar Processo / Download"],
            color="info",
            className="mt-1"
        ),
        dcc.Download(id="download"),
    ],
    style={
        'textAlign': 'center',
    },
)


@app.callback(
    Output('download', 'data'),
    Output('mensagem', 'children'),

    Input("btn", "n_clicks"),
    [Input('upload-files-div', 'isCompleted')],
    [State('upload-files-div', 'fileNames')],
    prevent_initial_call=True,
)
def display_files(isCompleted, fileNames, n_clicks):

    if not isCompleted:
        return 
    if fileNames is not None:

        folder_data = glob('data/*')[0]
        zip_file = glob('data/*/*.zip', recursive = True)[0]

        shutil.unpack_archive(zip_file, folder_data)

        shp_file = glob('data/**/*.shp', recursive = True)

        if shp_file:
            shp_file = shp_file[0]
            try:
                geo_df = gpd.read_file(shp_file,crs='4674')
                geo_df = geocod_add(geo_df)


                rdata_path = 'data/r_data/'
                os.mkdir(rdata_path)

                dest_file = rdata_path + shp_file.split('/')[-1]

                geo_df.to_file(dest_file,driver='ESRI Shapefile',encoding='UTF-8',index = False, crs="EPSG:4674")
                ffiles = glob(rdata_path + '*')

                shutil.rmtree(folder_data)
                shutil.make_archive(rdata_path, 'zip', rdata_path)

                uri = glob('data/*.zip')[0]


                return dcc.send_file('./data/r_data.zip'), dbc.Card([dbc.CardBody([html.P("Download Realizado!!!")])])
            except:
                return dbc.Card([dbc.CardBody([html.P('Algo deu errado :/ .', style=CARD_TEXT_STYLE2)])]), html.P("Algo deu errado! :/")
        else:
            return dbc.Card([dbc.CardBody([html.P('Shapefile não esta completo.', style=CARD_TEXT_STYLE2)])]), html.P("Algo deu errado! :/")
    else:
        return html.P('Treta'), html.P('Treta')



if __name__ == '__main__':
    app.run_server(debug=False)