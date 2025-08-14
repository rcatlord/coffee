#%%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium

#%%
df = pd.read_csv('data.csv')

#%%
""" m = folium.Map(location=[53.478213561808005,-2.244687230244309], zoom_start=13, tiles='cartodbpositron')
for row in df.iterrows():
    row_values = row[1]
    location = [row_values['lat'], row_values['lon']]
    popup = popup = '<strong>' + row_values['name'] + '</strong>'
    marker = folium.CircleMarker(location=location, 
                                 radius=5,
                                 color='black', fill_color='brown',
                                 popup=popup)
    marker.add_to(m)
m """

#%%
sf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs = 'EPSG:4326')
sf = sf[['name','address','url','geometry']]
sf.head()

# %%
map = sf.explore(
    tiles='CartoDB positron', 
    color='brown', 
    style_kwds={'color':'black', 'opacity':0.5, 'fillOpacity':0.1}, 
    marker_kwds={'radius':5}
)
map

# %%
map.save('map.html')

