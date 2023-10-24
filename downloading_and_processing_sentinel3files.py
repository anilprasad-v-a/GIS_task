# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:19:22 2023

@author: Legion
"""
# Downloading Sentinel 3 data using python


#installing eumdac package for downloading sentinal 3 data
#pip install  eumdac


import eumdac
import datetime
import shutil
# Insert your personal key and secret into the single quotes
consumer_key = 'qa88SaI8oAEkvXPs2uruI3L9Ttga'
consumer_secret = 'H8WpHfekE2diMSRFwGSRY93zngYa'

credentials = (consumer_key, consumer_secret)

token = eumdac.AccessToken(credentials)

print(f"This token '{token}' expires {token.expiration}")


# Add vertices for polygon, wrapping back to the start point.
#ploygon box created which includes the given sites lat and lon values

datastore = eumdac.DataStore(token)

#print(datastore.collections)
#'EO:EUM:DAT:0412' data store contains the SST files from 2021


selected_collection = datastore.get_collection('EO:EUM:DAT:0412')



ex=0.5
geometry = [[86.61137+ex, 20.24755+ex],[86.61137+ex, 20.96497+ex],[71.5649+ex, 20.96497+ex],[71.5649+ex, 20.24755+ex],[86.61137+ex, 20.24755+ex]]


# Set sensing start and end time
start = datetime.datetime(2023, 10, 18, 0, 0)
end = datetime.datetime(2023, 10, 18, 23, 59)


# Retrieve datasets that match our filter
products = selected_collection.search(
    geo='POLYGON(({}))'.format(','.join(["{} {}".format(*coord) for coord in geometry])),
    dtstart=start, 
    dtend=end)
    
print(f'Found Datasets: {len(products)} datasets for the given time range')

for product in products:
    print(str(product))
    
    
#downloading the avalibale sentinael 3 WST data in the region

import os

download_path = r"\path_to_folder\2023_10_18"  # Replace with your desired path

for product in products:
    with product.open() as fsrc, \
            open(os.path.join(download_path, fsrc.name), mode='wb') as fdst:
        shutil.copyfileobj(fsrc, fdst)
        print(f'Download of product {product} finished.')

print('All downloads are finished.')


###################necdf file loading and displaying meta data######################
import xarray as xr  # For handling multidimensional arrays and datasets

# Path where the data file is located
data = r"\path\202310~1.NC"

# Read the data as a dataset (DS) using the netcdf4 engine
DS = xr.open_dataset(data, engine='netcdf4')

# Show the metadata for the dataset
DS.info()  
# Access and display the coordinates of the dataset
DS.coords  

# Access and display the data variables in the dataset
DS.data_vars  

