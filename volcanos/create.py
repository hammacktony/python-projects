import pandas as pd
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster

FILENAME = 'data/volcanos.csv'


def get_data(FILENAME):
    """Reads data from csv and returns dataframe

    Arguments:
        FILENAME [Str] -- [Filename for csv for the volcano data.]

    Returns:
        [pandas.DataFrame] -- [DataFrame of data]
    """

    data = pd.read_csv(FILENAME)
    # Drop Unnecessary Columns
    data = data.drop(['Index', 'Region', 'Elev', 'Type'], axis=1)
    return data


def create_all(df):
    """Creates the map and adds all volcanoes to the map.

    Arguments:
        df {pandas.DataFrame} -- [pandas DataFrame of volcano data]

    Returns:
        [folium.FeatureGroup] -- [Folium FeatureGroup]
    """

    fg = folium.FeatureGroup(name="All Volcanoes", overlay=True)
    # Creates feature group
    cluster = MarkerCluster().add_to(fg)
    for row in df.itertuples():
        # Create markers and popups and add them to the cluster
        folium.Marker(location=[row.Latitude, row.Longitude],
                      popup=folium.Popup(row.Name, parse_html=True)).add_to(cluster)
    return fg


def create_layers(df, k, v):
    """Creates all the layers of which have different volcanoes plotted for specific time periods.

    Arguments:
        df {pandas.DataFrame} -- [pandas Dataframe of volcano data]
        k {dict.key} -- [description key name of title]
        v {dict.value} -- [description value of title]

    Returns:
        [folium.FeatureGroup] -- [FeatureGroup of mapped data]
    """

    sub_df = df.loc[df['Last KnownEruption'] == k]
    # Creates feature group
    fg = folium.FeatureGroup(name=v, overlay=True)
    # Creates Cluster
    cluster = MarkerCluster().add_to(fg)
    # Adds marker(s) to FeatureGroup
    for row in sub_df.itertuples():
        # Create markers and popups and add them to the cluster
        folium.Marker(location=[row.Latitude, row.Longitude],
                      popup=folium.Popup(row.Name, parse_html=True)).add_to(cluster)
    return fg


if __name__ == '__main__':
    """Reads data, creates main map, adds layers according to their specific descriptions and eras, and saves map as html.
    """
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
    my_map = folium.Map(
        location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=4)
    # Create Layer with all volcanoes
    my_map.add_child(create_all(df))
    #  Create Layers for Volcanoes that erupted in certain eras.
    for k, v in descriptions.items():
        my_map.add_child(create_layers(df, k, v))
    # Create Layer Control
    my_map.add_child(folium.LayerControl())
    # Save Map
    my_map.save('html/volcanoes.html')
