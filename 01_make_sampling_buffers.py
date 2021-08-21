# code to import locations and sample rasters in a buffer
import pandas as pd
import geopandas as gpd
from shapely.geometry import box
import math
import matplotlib.pyplot as plt
import numpy as np
import functools

# read in data
data_duke = pd.read_excel("data/raw/hair data_final.xlsx")
# data_guelph = pd.read_excel("data/raw/NewmanLab_Hair_Duke.xlsx")

# split data guelph coordinates column
# data_guelph[["lat", "lon"]] = data_guelph["Coordinates "].str.split(", ", 1, expand=True)
# data_guelph["lat"] = pd.to_numeric(data_guelph['lat'])
# data_guelph["lon"] = pd.to_numeric(data_guelph['lon'])

# select columns and assign site
data_sp = data_duke[["ID_hormone", "lat", "lon", "area"]]
data_sp.loc[data_sp.lon < -81.0, 'area'] = "Windsor"
# data_duke_sp["region"] = ["duke"] * len(data_duke_sp)
# data_guelph_sp = data_guelph[["Hair ID", "lat", "lon"]]
# data_guelph_sp["region"] = np.where(data_guelph_sp["lon"] > -80.5, "guelph", "detroit")

# rename sample id column
# data_sp = data_sp.rename(columns = {"ID_hormone" : "sample_id"})
# data_guelph_sp = data_guelph_sp.rename(columns = {"Hair ID" : "sample_id"})

# append data frames
# data_hormone_sp = pd.concat([data_duke_sp, data_guelph_sp])

# make spatial
data_sf = gpd.GeoDataFrame(data_sp, geometry=gpd.points_from_xy(data_sp.lon, data_sp.lat))
data_sf.set_crs(epsg=4326)
# write to file
data_sf.to_file(filename="data/spatial/data_cortisol_all_locs.gpkg", driver="GPKG")

# count unique coordinates
data_sf_count = data_sp.groupby(['lon', 'lat', 'area'], as_index=False).count()
data_sf_count = gpd.GeoDataFrame(data_sf_count,
                                 geometry=gpd.points_from_xy(data_sf_count.lon, data_sf_count.lat))
data_sf_count.set_crs(epsg=4326)
# export to file
data_sf_count.to_file(filename="data/spatial/data_cortisol_all_locs_guelph.gpkg", driver="GPKG")

# make buffer around point
area = 40000 # 4 hectares
radius = math.sqrt(area / math.pi)

# transform to correct UTM CRS
data_buffer = data_sf
data_buffer = data_buffer.set_crs(epsg=4326)
data_buffer = data_buffer.to_crs(epsg=32617)
data_buffer = data_buffer.buffer(distance=radius)
data_buffer = data_buffer.to_crs(epsg=4326)

# add sample id and region data
data_buffer = gpd.GeoDataFrame(data_sf[["ID_hormone", "lat", "lon", "area"]],
                               geometry=data_buffer)
# save
data_buffer.to_file(filename="data/spatial/data_cortisol_buffer.gpkg", driver="GPKG",
                    OVERWRITE="YES")
data_buffer.to_file(filename="data/spatial/data_cortisol_buffer.shp", OVERWRITE="YES")

## save bounding box by region
# first remove windsor
regions = ["Durham", "Guelph", "Windsor"]
bbox_list = []
for i in regions:
    data_bbox = data_buffer[data_buffer['area'] == i]['geometry'].total_bounds
    data_bbox = box(*data_bbox)
    data_bbox = gpd.GeoSeries(data_bbox)
    data_bbox = data_bbox.set_crs(epsg=4326)
    bbox_list.append(data_bbox)

# make single unioned polygon and export
bbox_list = functools.reduce(gpd.GeoSeries.union, bbox_list)
# split multipolygon
bbox_list = bbox_list.explode()

# save
bbox_list.to_file(filename="data/spatial/data_bboxes_cortisol.gpkg", driver="GPKG")
bbox_list.to_file(filename="data/spatial/data_bboxes_cortisol.shp")
