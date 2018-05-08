'''
Author: Tony Hammack
Date: 8 May, 2018
Version 1

This program uses folium to create an interactive plot of volcanoes. It also has layers of different volcanoes that have errupted
during a certain time period.

Special thanks to National Centers for Enviromental Information for volcano data.
'''

import pandas as pd
import requests
import folium
import numpy as np
from bs4 import BeautifulSoup

# Constants 
URL = 'https://www.ngdc.noaa.gov/nndc/struts/results?type_0=Like&query_0=&op_8=eq&v_8=&type_10=EXACT&query_10=None+Selected&le_2=&ge_3=&le_3=&ge_2=&op_5=eq&v_5=&op_6=eq&v_6=&op_7=eq&v_7=&t=102557&s=5&d=5'
FILENAME = 'data/volcanos.csv'
SAVENAME = 'data/volcanos.json'
MAPNAME = 'volcanos.html'


def get_data(URL,FILENAME):
	'''
	Loads data from url and saves it into a csv file.
	'''
	res = requests.get(URL)
	soup = BeautifulSoup(res.content,'lxml')
	table = soup.find_all('table')[2] 
	df = pd.read_html(str(table))
	out = df[0].to_csv()
	with open(FILENAME, 'w') as f:
		f.write(out)

def get_data(FILENAME):
	'''
	Gets data into data frame
	'''
	data = pd.read_csv(FILENAME)
	data = data.drop(columns='Index',axis=1)
	return data

def save_data(SAVENAME):
	'''
	Saves data to json
	'''
	df.to_json(path_or_buf=SAVENAME,orient='records')


def create_map(df):
	'''
	Creates the map template with all volcanos shown
	'''
	# Creates coordinates
	latAll = np.asarray(df['Latitude'])
	lonAll = np.asarray(df['Longitude'])
	nameAll = list(df['Volcano Name'])
	# Creates feature group
	fgAll = folium.FeatureGroup(name="All Volcanoes",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latAll,lonAll,nameAll):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgAll.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgAll

def create_D1(df):
	'''
	Last known eruption from 1964 and later.
	'''
	dfD1 = df.loc[df['Last KnownEruption']=='D1']
	# Creates coordinates
	latD1 = np.asarray(dfD1['Latitude'])
	lonD1 = np.asarray(dfD1['Longitude'])
	nameD1 = list(dfD1['Volcano Name'])
	# Creates feature group
	fgD1 = folium.FeatureGroup(name="Last known eruption from 1964 and later.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD1,lonD1,nameD1):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD1.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD1

def create_D2(df):
	'''
	Last known eruption 1900-1963.
	'''
	dfD2 = df.loc[df['Last KnownEruption']=='D2']
	# Creates coordinates
	latD2 = np.asarray(dfD2['Latitude'])
	lonD2 = np.asarray(dfD2['Longitude'])
	nameD2 = list(dfD2['Volcano Name'])
	# Creates feature group
	fgD2 = folium.FeatureGroup(name="Last known eruption 1900-1963.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD2,lonD2,nameD2):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD2.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD2

def create_D3(df):
	'''
	Last known eruption 1800-1899.
	'''
	dfD3 = df.loc[df['Last KnownEruption']=='D3']
	# Creates coordinates
	latD3 = np.asarray(dfD3['Latitude'])
	lonD3 = np.asarray(dfD3['Longitude'])
	nameD3 = list(dfD3['Volcano Name'])
	# Creates feature group
	fgD3 = folium.FeatureGroup(name="Last known eruption 1800-1899.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD3,lonD3,nameD3):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD3.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD3

def create_D4(df):
	'''
	Last known eruption 1700-1799.
	'''
	dfD4 = df.loc[df['Last KnownEruption']=='D4']
	# Creates coordinates
	latD4 = np.asarray(dfD4['Latitude'])
	lonD4 = np.asarray(dfD4['Longitude'])
	nameD4 = list(dfD4['Volcano Name'])
	# Creates feature group
	fgD4 = folium.FeatureGroup(name="Last known eruption 1700-1799.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD4,lonD4,nameD4):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD4.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD4

def create_D5(df):
	'''
	Last known eruption 1500-1699.
	'''
	dfD5 = df.loc[df['Last KnownEruption']=='D5']
	# Creates coordinates
	latD5 = np.asarray(dfD5['Latitude'])
	lonD5 = np.asarray(dfD5['Longitude'])
	nameD5 = list(dfD5['Volcano Name'])
	# Creates feature group
	fgD5 = folium.FeatureGroup(name="Last known eruption 1500-1699.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD5,lonD5,nameD5):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD5.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD5

def create_D6(df):
	'''
	Last known eruption A.D. 1-1499.
	'''
	dfD6 = df.loc[df['Last KnownEruption']=='D6']
	# Creates coordinates
	latD6 = np.asarray(dfD6['Latitude'])
	lonD6 = np.asarray(dfD6['Longitude'])
	nameD6 = list(dfD6['Volcano Name'])
	# Creates feature group
	fgD6 = folium.FeatureGroup(name="Last known eruption A.D. 1-1499.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD6,lonD6,nameD6):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD6.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD6

def create_D7(df):
	'''
	Last known eruption B.C. (Holocene)
	'''
	dfD7 = df.loc[df['Last KnownEruption']=='D7']
	# Creates coordinates
	latD7 = np.asarray(dfD7['Latitude'])
	lonD7 = np.asarray(dfD7['Longitude'])
	nameD7 = list(dfD7['Volcano Name'])
	# Creates feature group
	fgD7 = folium.FeatureGroup(name="Last known eruption B.C. (Holocene)",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latD7,lonD7,nameD7):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgD7.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgD7

def create_DFU(df):
	'''
	Undated, but probable Holocene eruption.
	'''
	dfU = df.loc[df['Last KnownEruption']=='U']
	# Creates coordinates
	latU = np.asarray(dfU['Latitude'])
	lonU = np.asarray(dfU['Longitude'])
	nameU = list(dfU['Volcano Name'])
	# Creates feature group
	fgU = folium.FeatureGroup(name="Undated, but probable Holocene eruption.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latU,lonU,nameU):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgU.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgU

def create_DQ(df):
	'''
	Quaternary eruption(s) with the only known Holocene activity being hydrothermal.
	'''
	dfQ = df.loc[df['Last KnownEruption']=='Q']
	# Creates coordinates
	latQ = np.asarray(dfQ['Latitude'])
	lonQ = np.asarray(dfQ['Longitude'])
	nameQ = list(dfQ['Volcano Name'])
	# Creates feature group
	fgQ = folium.FeatureGroup(name="Quaternary eruption(s) with the only known Holocene activity being hydrothermal.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latQ,lonQ,nameQ):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgQ.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgQ

def create_dfQuestion(df):
	'''
	Uncertain Holocene eruption.
	'''
	dfQuestion = df.loc[df['Last KnownEruption']=='?']
	# Creates coordinates
	latQuestion = np.asarray(dfQuestion['Latitude'])
	lonQuestion = np.asarray(dfQuestion['Longitude'])
	nameQuestion = list(dfQuestion['Volcano Name'])
	# Creates feature group
	fgQuestion = folium.FeatureGroup(name="Uncertain Holocene eruption.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latQuestion,lonQuestion,nameQuestion):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgQuestion.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgQuestion

def create_dfUnknown(df):
	'''
	Unknown eruption date.
	'''
	dfUnkown = df.loc[df['Last KnownEruption']=='Unknown']
	# Creates coordinates
	latUnknown = np.asarray(dfUnkown['Latitude'])
	lonUnknown = np.asarray(dfUnkown['Longitude'])
	nameUnknown = list(dfUnkown['Volcano Name'])
	# Creates feature group
	fgUnknown = folium.FeatureGroup(name="Unknown eruption date.",overlay=True)
	# Adds marker(s) to FeatureGroup
	for lt,ln,nm in zip(latUnknown,lonUnknown,nameUnknown):
		if not (np.isfinite([lt,ln])).all(): # Checks to see if entries are NaN
			continue
		else:
			# Creates Markers, parse_html to make sure apostrophe's work
			fgUnknown.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(str(nm),parse_html=True),icon=folium.Icon(color='green')))
	return fgUnknown


if __name__ == '__main__':
	# Get dataframe
	df = get_data(FILENAME)
	# Creates the map object centered in the moddle of the Atlantic
	map = folium.Map(location=[33.13521647785765,-41.86843012500003],tiles='Stamen Terrain',zoom_start=2)
	#Adds feature groups to map
	map.add_child(create_map(df))
	map.add_child(create_D1(df))
	map.add_child(create_D2(df))
	map.add_child(create_D3(df))
	map.add_child(create_D4(df))
	map.add_child(create_D5(df))
	map.add_child(create_D6(df))
	map.add_child(create_D7(df))
	map.add_child(create_DFU(df))
	map.add_child(create_DQ(df))
	map.add_child(create_dfQuestion(df))
	map.add_child(create_dfUnknown(df))
	# Adds Layer control to map
	map.add_child(folium.LayerControl())
	# Saves map file
	map.save(MAPNAME)
	
