
# for file listing
import os
# for spatial data
import pandas as pd
import geopandas as gpd

# for zipping
from zipfile import ZipFile

# check wd
os.getcwd()

# list transects
mypath = "data/spatial"
transects = [mypath + "/" + f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

# filter for gpx
transects = [f for f in transects if "gpx" in f]

# read transects
transects = list(map(lambda f: gpd.read_file(f, layer='tracks'), transects))

# join transects
transects = gpd.GeoDataFrame( pd.concat( transects, ignore_index=True) )

# export as shapefile
transects.to_file(mypath + "/" + "transects_all.shp")

# list transect files and zip
transects = [mypath + "/" + f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

# filter for gpx
transects = [f for f in transects if "transects_all" in f]

# zip together
# create a ZipFile object
zipObj = ZipFile(mypath + "/" + "transects_all.zip", "w")
# Add multiple files to the zip
for f in transects:
    zipObj.write(f)
# close the Zip File
zipObj.close()