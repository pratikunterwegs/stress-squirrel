# code to import locations and sample rasters in a buffer
import geopandas
import pandas as pd
import geopandas as gpd
from shapely.geometry import box
import math

# read in data
data = pd.read_excel("data/raw/hair data.xlsx")
# make spatial
data_sf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.lon, data.lat))
data_sf.set_crs(epsg=4326)
# write to file
data_sf.to_file(filename="data/spatial/data_cortisol_duke.gpkg", driver="GPKG")

# count unique coordinates
data_sf_count = data.groupby(['lon', 'lat'])['lon', 'lat'].count()
data_sf_count = gpd.GeoDataFrame(data_sf_count,
                                 geometry=gpd.points_from_xy(data_sf_count.lon, data_sf_count.lat))
data_sf_count.set_crs(epsg=4326)
# export to file
data_sf_count.to_file(filename="data/spatial/data_cortisol_count_duke.gpkg", driver="GPKG")

# make buffer around point
area = 40000 # 4 hectares
radius = math.sqrt(area / math.pi)

# transform to correct UTM CRS
data_buffer = data_sf.to_crs(epsg=32617)
data_buffer = data_buffer.buffer(distance=radius)
# save bounding box
data_bbox = data_buffer.total_bounds
data_bbox = box(*data_bbox)
data_bbox = gpd.GeoSeries(data_bbox)
data_bbox.to_file(filename="data/spatial/data_cortisol_bbox.shp")