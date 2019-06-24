# Based on http://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html#from-wkt-format

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from shapely import wkt

df = pd.DataFrame({'City': ['Buenos Aires'], 'Country': ['Argentina'], 'Coordinates': ['POINT(-34.58 -58.66)']})
df['Coordinates'] = df['Coordinates'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(df, geometry='Coordinates')

print(gdf.head())

# expect-output-to-have: Buenos Aires POINT (-34.58 -58.66) Argentina
