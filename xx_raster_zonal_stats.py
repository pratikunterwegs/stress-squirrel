import rasterio
from rasterio.plot import show
import math
from rasterstats import zonal_stats
import matplotlib.pyplot as plt

# rescale ndbi 0 - 1
ndbi = rasterio.open("data/raster/duke_guelph_ndbi_cortisol.tif")
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
for name,file in zip(['ndvi', 'ndbi'], ['data/raster/duke_guelph_ndvi_cortisol.tif',
                                        'data/raster/duke_guelph_ndbi_cortisol.tif']):
    zs = zonal_stats("data/spatial/data_cortisol_buffer.gpkg", file,
                    stats = ['mean','median','std'])
    zs = pd.DataFrame(zs)
    zs.rename(columns={'mean':(name + "_" + "mean"), 'std':(name + "_" + "sd"), 'median':(name + "_" + "median")}, inplace=True)
    data_raster.append(zs)

data_raster = pd.concat(data_raster, axis=1)

# link to data
data = pd.concat([data, data_raster], axis=1).drop(columns="geometry")

# save file
data.to_csv("data/data_cortisol_environmental_data.csv")
