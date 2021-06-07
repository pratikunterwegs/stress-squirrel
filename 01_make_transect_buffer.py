# code to make transect buffers
import pandas as pd
import geopandas as gpd
import fiona
import glob

# list files
transects = glob.glob("data/raw/*.gpx")
# read in files with geopandas
tmplist = []
for i in transects:
    tmpread = fiona.open(i, layer="tracks")
    tmpread = gpd.GeoDataFrame.from_features(tmpread)
    tmplist.append(tmpread)

# convert to geopandas
transects = pd.concat(tmplist)
transects = gpd.GeoDataFrame(transects)

# buffer by 200 metres
buffer = transects
buffer = buffer.set_crs(epsg=4326).to_crs(epsg=32617)
buffer = buffer.buffer(distance=200)
buffer = buffer.to_crs(epsg=4326)

# write to file
transects = transects.drop(columns="geometry")
transects.geometry = buffer
transects.to_file(filename="data/raw/transects_all.shp")

# get box and save
data_bbox = buffer.total_bounds
data_bbox = box(*data_bbox)
data_bbox = gpd.GeoSeries(data_bbox)
data_bbox.to_file(filename="data/spatial/transect_bbox.shp")
