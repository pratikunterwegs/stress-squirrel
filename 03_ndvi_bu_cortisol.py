# code to import locations and sample rasters in a buffer
import geopandas
import pandas as pd
import geopandas as gpd
from shapely.geometry import box
import rasterio
from rasterio.plot import show
import math
from rasterstats import zonal_stats
import matplotlib.pyplot as plt
import numpy as np

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
data_buffer = data_sf
data_buffer = data_buffer.set_crs(epsg=4326)
data_buffer = data_buffer.to_crs(epsg=32617)
data_buffer = data_buffer.buffer(distance=radius)
data_buffer = data_buffer.to_crs(epsg=4326)
# save
data_buffer.to_file(filename="data/spatial/data_cortisol_buffer.gpkg", driver="GPKG",
                    OVERWRITE="YES")

# save bounding box
data_bbox = data_buffer.total_bounds
data_bbox = box(*data_bbox)
data_bbox = gpd.GeoSeries(data_bbox)
data_bbox.to_file(filename="data/spatial/data_cortisol_bbox.shp")

# rescale ndbi 0 - 1
ndbi = rasterio.open("data/spatial/duke_built_up_cortisol.tif")
profile = ndbi.profile
ndbi_array = ndbi.read(1)
ndbi_array[ndbi_array < -2] = np.nan

# rescale
ndbi_array = ndbi_array - (np.nanmin(ndbi_array)) \
             / np.ptp(ndbi_array[np.isnan(ndbi_array) == False])
# plot to check
plt.imshow(ndbi_array, cmap='cividis')
plt.colorbar()
plt.show()

#### WORK IN PROGRESS ####

#save scaled array
ndbi_write = rasterio.open("data/spatial/duke_built_up_cortisol.tif", 'w', **profile)
ndbi_write.write(ndbi_array.astype(rasterio.float32), 1)
ndbi_write.close()

# get zonal stats
data_raster = []
for name,file in zip(['ndvi', 'ndbi'], ['data/spatial/duke_ndvi_cortisol.tif', 'data/spatial/duke_built_up_cortisol.tif']):
    zs = zonal_stats("data/spatial/data_cortisol_buffer.gpkg", file, 
                    stats = ['mean','median','std'])
    zs = pd.DataFrame(zs)
    zs.rename(columns={'mean':(name + "_" + "mean"), 'std':(name + "_" + "sd"), 'median':(name + "_" + "median")}, inplace=True)
    data_raster.append(zs)

data_raster = pd.concat(data_raster, axis=1)

# link to data
data = pd.concat([data, data_raster], axis=1).drop(columns="geometry")

# save file
data.to_csv("data/data_cortisol_environmental_data_test.csv")
