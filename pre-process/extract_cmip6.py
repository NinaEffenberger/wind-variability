import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
)

six_hours_v = "bigdata/CMIP/vas_6hrPlev_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010300-200912312100.nc"
six_hours_u = "bigdata/CMIP/uas_6hrPlev_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010300-200912312100.nc"
three_hours_v = "bigdata/CMIP/vas_E3hr_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010130-200912312230.nc"
three_hours_u = "bigdata/CMIP/uas_E3hr_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010130-200912312230.nc"

day_v = "bigdata/CMIP/vas_day_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_19900101-20091231.nc"
day_u = "bigdata/CMIP/uas_day_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_19900101-20091231.nc"


six_hours_pt_v = "bigdata/CMIP/vas_6hrPlevPt_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010600-201001010000.nc"
six_hours_pt_u = "bigdata/CMIP/uas_6hrPlevPt_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010600-201001010000.nc"
three_hours_pt_v = "bigdata/CMIP/vas_3hr_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010300-201001010000.nc"
three_hours_pt_u = "bigdata/CMIP/uas_3hr_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_199001010300-201001010000.nc"

# Aachen
lon = 6.0941
lat = 50.7827

savepath = "data/cmip6/data/Aachen"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)

# Boltenhagen
lon = 11.19
lat = 54.00

savepath = "data/cmip6/data/Boltenhagen"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantanoeus_three.npy", three_hours_pt_v.time.values)

# Zugspitze
lon = 10.98
lat = 47.42

savepath = "data/cmip6/data/Zugspitze"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)
# Fichtelberg
lon = 11.84
lat = 49.98

savepath = "data/cmip6/data/Fichtelberg"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)

# Kelmarsh
lon = 360 - 0.95
lat = 52.40

savepath = "data/cmip6/data/Kelmarsh"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)

# Penmanshiel
lon = 360 - 2.31
lat = 55.90

savepath = "data/cmip6/data/Penmanshiel"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)

# Owez
lon = 4.39
lat = 52.61

savepath = "data/cmip6/data/Owez"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)

# NWTC
lon = 360 - 105.23
lat = 39.21

savepath = "data/cmip6/data/NWTC"
six_hours_v = xr.open_dataset(six_hours_v)
six_hours_u = xr.open_dataset(six_hours_u)
time_series_six_hours_u = six_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_v = six_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six = np.sqrt(time_series_six_hours_u**2 + time_series_six_hours_v**2)
np.save(savepath + "/time_series_six.npy", time_series_six)

three_hours_v = xr.open_dataset(three_hours_v)
three_hours_u = xr.open_dataset(three_hours_u)
time_series_three_hours_u = three_hours_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_v = three_hours_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three = np.sqrt(time_series_three_hours_u**2 + time_series_three_hours_v**2)
np.save(savepath + "/time_series_three.npy", time_series_three)
np.save(savepath + "/times_averages_three.npy", three_hours_v.time.values)

day_v = xr.open_dataset(day_v)
day_u = xr.open_dataset(day_u)
time_series_day_u = day_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_day_v = day_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_day = np.sqrt(time_series_day_u**2 + time_series_day_v**2)
np.save(savepath + "/time_series_day.npy", time_series_day)

six_hours_pt_v = xr.open_dataset(six_hours_pt_v)
six_hours_pt_u = xr.open_dataset(six_hours_pt_u)
time_series_six_hours_pt_u = six_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_six_hours_pt_v = six_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_six_pt = np.sqrt(time_series_six_hours_pt_u**2 + time_series_six_hours_pt_v**2)
np.save(savepath + "/time_series_six_pt.npy", time_series_six_pt)

three_hours_pt_v = xr.open_dataset(three_hours_pt_v)
three_hours_pt_u = xr.open_dataset(three_hours_pt_u)
time_series_three_hours_pt_u = three_hours_pt_u.sel(lat=lat, lon=lon, method="nearest").uas
time_series_three_hours_pt_v = three_hours_pt_v.sel(lat=lat, lon=lon, method="nearest").vas
time_series_three_pt = np.sqrt(time_series_three_hours_pt_u**2 + time_series_three_hours_pt_v**2)
np.save(savepath + "/time_series_three_pt.npy", time_series_three_pt)
np.save(savepath + "/times_instantaneous_three.npy", three_hours_pt_v.time.values)
