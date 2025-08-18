#%%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium

#%%
df = pd.read_csv('data.csv')

#%%
map = folium.Map(location=[53.478213561808005,-2.244687230244309], zoom_start=15, tiles='CartoDB positron')
for index, row in df.iterrows():
    latitude = row['lat']
    longitude = row['lon']
    text = f"""<a href="{row['url']}" target="_blank">{row['name']}</a><br>{row['address']}"""

    folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(text, max_width=2650),
        icon=folium.Icon(color='red', icon='mug-saucer', prefix='fa')
    ).add_to(map)
map.save('map.html')

## Alternatively

#%%
sf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs = 'EPSG:4326')
sf = sf[['name','address','url','geometry']]
sf.head()

# %%
title = f'<h1 style="position:absolute;z-index:100000;left:30vw;">Coffee shops</h1>'
map = sf.explore(
    tiles='CartoDB positron', 
    marker_type='marker',
    marker_kwds={'icon': folium.map.Icon(color='red', icon='mug-saucer', prefix='fa')},
    tooltip = False, 
    popup=True,
    popup_kwds={"aliases": ["Name", "Address", "Website"]}
)
map.get_root().html.add_child(folium.Element(title))
map

# %%
map = folium.Map(location=[53.478213561808005,-2.244687230244309], zoom_start=13)
folium.GeoJson(
    sf,
    popup=folium.GeoJsonPopup(
        fields=['name','address','url'],
        aliases=['Name','Address','Link'])
).add_to(map)
map