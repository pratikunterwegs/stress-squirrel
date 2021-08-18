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

# check
data.head()

# rescale ndbi between 0 and 1
data.ndbi_mean = (data.ndbi_mean - min(data.ndbi_mean)) / \
    (max(data.ndbi_mean) - min(data.ndbi_mean))

# save
data.to_csv("data/data_zonalstats_all_locs.csv", index=False)

# read full dataset and join by area and location
full_data = pd.read_excel("data/raw/correct locations.xlsx")
# remove old zonal stats
full_data = full_data.drop(axis = 1, columns = ['ndvi_mean', 'built_up_mean', 'ndvi_sd', 'built_up_sd'])
# join
full_data = pd.concat([full_data, data], axis = 1)

# save full data
full_data.to_csv("data/data_cortisol_all_locs.csv", index=False)

# check with figure
sns.scatterplot(x = "ndvi_mean", y = "ndbi_mean", hue = "area",
                data = data)
plt.savefig("figures/fig_ndvi_ndbi_zonal_stats_gee_18_aug_21.png")
