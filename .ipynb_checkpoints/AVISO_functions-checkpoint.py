# Functions to work with AVISO eddy atlas data

# LJK
# Date created: 04/10/24
# Last edited: 04/10/24

import xarray as xr
import numpy as np
from itertools import groupby
from matplotlib.path import Path


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def get_LBE(ds,eddy_date):
    """
    ds: netCDF AVISO format
    eddy_date: date in format 'YYYY-MM-DD'

    Returns contour lons, contour lats, center lon, center lat, eddy ID
    """
    
    ind = np.where(ds.time == np.datetime64(eddy_date))[0][0]
    contour_lons = np.array(ds.effective_contour_longitude[ind])
    contour_lats = np.array(ds.effective_contour_latitude[ind])

    if all_equal(contour_lons): 
        print('There was no eddy data on this day...')

    return contour_lons,contour_lats,ds.longitude[ind],ds.latitude[ind],ds.track[ind]

def get_eddy_by_ID_date(ds,track_id,eddy_date):
    """
    ds: netCDF AVISO format
    track_id: id of eddy to extract
    eddy_date: date in format 'YYYY-MM-DD'

    Returns contour lons, contour lats, center lon, center lat
    """
    try:
        ind = np.where((ds.track == track_id) & (ds.time == np.datetime64(eddy_date)))[0][0]
        contour_lons = np.array(ds.effective_contour_longitude[ind])
        contour_lats = np.array(ds.effective_contour_latitude[ind])
    except:
        print('No eddy data available with that request ... :(')        
    
    return contour_lons,contour_lats,ds.longitude[ind],ds.latitude[ind]

def in_eddy(ds,float_lat,float_lon,float_time):
    """
    float_lat: degrees north
    float_lon: degrees east
    float_time: should be in format 'YYYY-MM-DD'
    """

    in_eddy_flag = False 

    float_time = np.datetime64(float_time)
    if float_time in ds.time: # some dates not in dateset        
        for i in np.where(ds.time == float_time)[0]: # usually will only be 1 eddy, but sometimes there are 2 after a split
            contour_lons = np.array(ds.effective_contour_longitude[i]) # eddy lons
            contour_lats = np.array(ds.effective_contour_latitude[i]) # eddy lats
            
            if all_equal(contour_lons): # eddy break
                pass
            else:
                poly = Path([(contour_lats[j],contour_lons[j]) for j in np.arange(0,len(contour_lats))]) # set up the polygon
                if poly.contains_points([(float_lat,float_lon)]): #find if point is inside the polygon
                    in_eddy_flag = True 

    return in_eddy_flag