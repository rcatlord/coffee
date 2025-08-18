# Coffe shops in Manchester

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

df = pd.read_csv("data.csv")
df.head()

st.set_page_config(page_title="MCR coffee shops", page_icon=":coffee:", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("MCR Coffee shops ☕")
st.markdown('''Explore some of the best independent coffee shops in Manchester:''')

map = folium.Map(location=[53.478213561808005,-2.244687230244309], zoom_start=15, tiles='CartoDB positron')
for index, row in df.iterrows():
    latitude = row['lat']
    longitude = row['lon']
    text = f"""<a href="{row['url']}" target="_blank">{row['name']}</a><br>{row['address']}"""

    folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(text, max_width=200),
        icon=folium.Icon(color='red', icon='mug-saucer', prefix='fa')
    ).add_to(map)
st_folium(map, width=700, height=500)

st.markdown('''Or scroll through the complete list:''')

st.dataframe(df[['name','address','url']], 
             column_config={
                 "name": "Name",
                 "address": "Address",
                 "url": st.column_config.LinkColumn("More details")
             },
             hide_index=True)