# prelim code for earth engine landcover around duke

# import libs
import ee
import folium
import foliumgee
from IPython.display import Image, display
ee.Initialize()
# ee.Authenticate()

import ee
import pandas as pd

ee.Initialize()

# get transects from user assets
downtown = ee.FeatureCollection("users/pratik_unterwegs/transect_squirrel_downtown")
forest = ee.FeatureCollection("users/pratik_unterwegs/transect_squirrel_forest")

# combine transects
transects = downtown.merge(forest)

# get a 1km buffer
buffer_size_m = 1000
transect_buffer = transects.geometry()
transect_buffer = transect_buffer.buffer(buffer_size_m)

# define start and end date
start_date = '2019-05-01'
end_date = '2019-10-01'


# define a crop function for the transect buffer only
def crop_to_transect(image):
    image_clip = image.clip(transect_buffer)
    return image_clip


# get sentinel data
sentinel = ee.ImageCollection("COPERNICUS/S2")\
  .filterDate(start_date, end_date)\
  .map(crop_to_transect)

# # remove clouds
# def remove_clouds(image):
#     quality = image.select("QA60")
#     quality = quality.unmask()
#     cloud_01 = quality.gt(0)
#     cloud_mask = image.mask().and(cloud_01.not())
#     return image.updateMask(cloud_mask)

# now remove the clouds
# sentinel_cloudfree = sentinel.map(remove_clouds)

# adding a NDVI band
def add_ndvi(image):
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('ndvi')
    return image.addBands([ndvi])

# map ndvi over sentinel
sentinel_ndvi = sentinel.map(add_ndvi)

# get median values
ndvi_median = sentinel_ndvi.select('ndvi').mean()

