import pandas as pd
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster

FILENAME = 'data/volcanos.csv'

def get_data(FILENAME):
    '''
    Gets data into data frame
    '''
    data = pd.read_csv(FILENAME)
    data = data.drop(['Index', 'Region', 'Elev', 'Type'],axis=1)
    return data


def create_all(df):
    fg = folium.FeatureGroup(name="All Volcanoes",overlay=True)
    cluster = MarkerCluster().add_to(fg)
    #creating a Marker for each point in df_sample. Each point will get a popup with their zip
    for row in df.itertuples():
        folium.Marker(location=[row.Latitude,row.Longitude],
               popup=folium.Popup(row.Name,parse_html=True)).add_to(cluster)
    return fg
    
def create_layers(df, k,v):
    sub_df = df.loc[df['Last KnownEruption']== k]
#     mc = MarkerCluster()
    # Creates feature group
    fg = folium.FeatureGroup(name=v,overlay=True)
    cluster = MarkerCluster().add_to(fg)
    # Adds marker(s) to FeatureGroup
    for row in sub_df.itertuples():
        # Creates Markers, parse_html to make sure apostrophe's work
        folium.Marker(location=[row.Latitude,row.Longitude],
           popup=folium.Popup(row.Name,parse_html=True)).add_to(cluster)
#     fg.add_child(mc)
    return fg

if __name == '__main__':
    df = get_data(FILENAME)
    descriptions = {'D1': 'Last known eruption from 1964 and later', 
               'D2': 'Last known eruption 1900-1963',
               'D3': 'Last known eruption 1800-1899', 
               'D4': 'Last known eruption 1700-1799', 
               'D5': 'Last known eruption 1500-1699',
               'D6': 'Last known eruption A.D. 1-1499',
               'D7': 'Last known eruption B.C. (Holocene)',
                'U': 'Undated, but probable Holocene eruption',
                'Q': 'Quaternary eruption(s) with the only known Holocene activity being hydrothermal',
                '?': 'Uncertain Holocene eruption',
                'Unknown': 'Unknown eruption date'
               }
    # Create Map
    my_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=4)
    my_map.add_child(create_all(df))
    for k,v in descriptions.items():
        my_map.add_child(create_layers(df, k, v)) 
    my_map.add_child(folium.LayerControl())
    my_map.save('volcanoes.html')