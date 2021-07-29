# Code to import zonal stats from GEE and link to samples.

import pandas as pd
import functools
import seaborn as sns
import matplotlib.pyplot as plt

# get zonal stats
data_list = []
for measure in ['ndvi', 'ndbi']:
    mean = pd.read_csv("data/" + measure + "_mean_duke_guelph.csv")
    mean = mean.rename(columns = {"mean" : measure + "_mean"})
    mean = mean.drop(columns=['system:index'])
    sd = pd.read_csv("data/" + measure + "_std_duke_guelph.csv")
    sd = sd.rename(columns = {"stdDev" : measure + "_sd"})
    sd = sd.drop(columns=['system:index'])
    data = pd.merge(mean, sd, on = ['sample_id', 'lat', 'lon', 'region'])
    data_list.append(data)

# merge list
data = functools.reduce(pd.merge, data_list)

# check
data.head()

# save
data.to_csv("data/data_cortisol_duke_guelph.csv", index=False)

# check with figure
sns.scatterplot(x = "ndvi_mean", y = "ndbi_mean", hue = "region",
                data = data)
plt.savefig("figures/fig_ndvi_ndbi_zonal_stats_gee_29_jul_21.png")
