# -*- coding: utf-8 -*-

"""
Created on Tue Oct 24 16:01:19 2023
@author: Legion
"""

# Import the necessary libraries
import rasterio  # For working with geospatial data

# Open the GeoTIFF file containing Sea Surface Temperature data (site2)
data = rasterio.open(r".\path\SST_DATA_1.tif")

# The exported GeoTIFF file has two bands, where band 0 is a grayscale band and band 1 contains temperature values.
# Read data from the first band (band 1)
z = data.read()[1]

# Check the Coordinate Reference System (CRS) of the data
data.crs

# Check the bounding box (extent) of the data
data.bounds

# Since the raster is in a regular lon/lat grid (EPSG:4326), we can use `data.index()` to identify the index of a given lon/lat pair.
# (It expects coordinates in the native CRS of the data)

# Define a function to retrieve the Sea Surface Temperature at a specific lon/lat location
def getval(lon, lat):
    idx = data.index(lon, lat, precision=1E-6)
    print("Sea Surface Temperature of location:", z[idx])
    return

# Example: Get the Sea Surface Temperature at a specific location (site 2)
getval(71.5649, 20.96497)  # Location of site 2
