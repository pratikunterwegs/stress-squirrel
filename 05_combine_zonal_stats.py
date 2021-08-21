# Code to import zonal stats from GEE and link to samples.

import pandas as pd
import functools
import seaborn as sns
import matplotlib.pyplot as plt

# get zonal stats
data_list = []
for measure in ['ndvi', 'ndbi']:
    mean = pd.read_csv("data/data_zonalstats_" + measure + "_mean.csv")
    mean = mean.rename(columns = {"mean" : measure + "_mean"})
    mean = mean.drop(columns=['system:index'])
    sd = pd.read_csv("data/data_zonalstats_" + measure + "_std.csv")
    sd = sd.rename(columns = {"stdDev" : measure + "_sd"})
    sd = sd.drop(columns=['system:index'])
    data = pd.merge(mean, sd, on = ['ID_hormone', 'lat', 'lon', 'area'])
    data_list.append(data)

# merge list
data = functools.reduce(pd.merge, data_list)

data.loc[data.lon < -81.0, 'area'] = "Windsor"
# check
data.head()

# rescale ndbi between 0 and 1
# data.ndbi_mean = (data.ndbi_mean - min(data.ndbi_mean)) / \
#     (max(data.ndbi_mean) - min(data.ndbi_mean))

# save
data.to_csv("data/data_zonalstats_all_locs.csv", index=False)
# remove all but id hormone
data = data[['ID_hormone', 'ndvi_mean', 'ndvi_sd', 'ndbi_mean', 'ndbi_sd']]
data['ID_hormone'] = data['ID_hormone'].astype("str")

# read full dataset and join by area and location
full_data = pd.read_excel("data/raw/hair data_final.xlsx")
# remove old zonal stats
full_data = full_data.drop(axis = 1, columns = ['ndvi_mean', 'built_up_mean', \
    'ndvi_sd', 'built_up_sd', 'ndvi_median', 'built_up_median'])
# make string ID hormone
full_data['ID_hormone'] = full_data['ID_hormone'].astype('str')

# join
full_data = pd.merge(full_data, data, on=['ID_hormone'])

# save full data
full_data.to_csv("data/data_cortisol_all_locs.csv", index=False)

# check with figure
sns.scatterplot(x = "ndvi_mean", y = "ndbi_mean", hue = "area",
                data = full_data)
plt.savefig("figures/fig_ndvi_ndbi_zonal_stats_gee_18_aug_21.png")
