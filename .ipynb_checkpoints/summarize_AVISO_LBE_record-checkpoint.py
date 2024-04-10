# Summarize AVISO track IDs length of time in ds and break dates
# LJK
# 04/10/24

import csv
import xarray as xr
import numpy as np
from AVISO_functions import *

# open ds
ds = xr.open_dataset('/nfs/micklab005/jonesae/BGCargo_LBE_eddy/META3.2_DT_allsat_Anticyclonic_long_LBE.nc')

# Set up CSV
track_info = [['ID','Start_date','End_date','Length_days','Num_breaks','Break_dates']]
for t in np.unique(ds.track):
    inds = np.where(ds.track == t)[0]
    
    breaks = []
    for i in inds:
        contour_lons = np.array(ds.effective_contour_longitude[i])
        if all_equal(contour_lons):
            breaks.append(ds.time[i].values.astype('str')[0:10])

    track_info.append([t,ds.time[inds[0]].values.astype('str')[0:10],ds.time[inds[-1]].values.astype('str')[0:10],
                 (np.array(ds.time[inds[-1]])-np.array(ds.time[inds[0]])).astype('timedelta64[D]').astype('int'),len(breaks),breaks])

save_dir = '/nfs/micklab005/jonesae/BGCargo_LBE_eddy/'
with open(save_dir + 'AVISO_LBE_track_summary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(track_info)