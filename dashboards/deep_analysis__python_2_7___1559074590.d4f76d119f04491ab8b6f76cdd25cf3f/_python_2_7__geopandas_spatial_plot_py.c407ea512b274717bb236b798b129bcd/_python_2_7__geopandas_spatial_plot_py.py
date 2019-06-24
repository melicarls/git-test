# Based on http://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html#from-longitudes-and-latitudes

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

df = pd.DataFrame({'City': ['Buenos Aires'], 'Country': ['Argentina'], 'Latitude': [-34.58], 'Longitude': [-58.66]})
df['Coordinates'] = list(zip(df.Longitude, df.Latitude))
df['Coordinates'] = df['Coordinates'].apply(Point)

gdf = gpd.GeoDataFrame(df, geometry='Coordinates')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world[world.continent == 'South America'].plot(color='white', edgecolor='black')
gdf.plot(ax=ax, color='red')

periscope.output(plt)

# expect-image
