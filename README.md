# Urbanisation around Durham and Guelph

This is source code to extract an urbanisation index from remote sensing data, around squirrel trapping locations in North America.

## Code

- `01_make_sampling_buffers.py` Make 40 hectare buffers around the sampling location.

- `02_zonal_statistics.ipynb` Get zonal NDVI and NDBI for the buffered sampling locations.

- `03_combine_zonal_stats.py` Combine NDVI and NDBI measures.

## Caveats

Zonal statistics rely on Google Earth Engine, which requires an account, and to install the `ee` and `geemap` packages. The easiest way to do the latter is by following the setup guide on the `geemap` homepage. A Conda environment for `gee` is advised.
