import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
from distributions import (
    compute_instantenous_windspeeds,
    plot_param_trend,
    plot_param_trend_both,
    plot_param_trend_instanteous,
    plot_param_trend_precentage,
    plot_param_trend_precentage_instanteous,
    weibull_paramsdef,
    weibull_paramsdef_instanteous,
)
from windspeed_averages_wp import (
    compute_average_windspeeds,
    drop_nans,
    drop_nans_DWD,
    load_data,
    set_date,
    set_date_DWD,
)

# load data
average_10min = np.load("data/Pickles/Aachen/first_three_years/average_10min.npy")
day = np.load("data/Pickles/Aachen/first_three_years/day.npy")
six_hour = np.load("data/Pickles/Aachen/first_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/first_three_years/three_hour.npy")
hour = np.load("data/Pickles/Aachen/first_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/first_three_years_instantaneous/cs_aachen.npy", cs)
np.save("data/weibull_params/first_three_years_instantaneous/scales_aachen.npy", scales)
np.save("data/weibull_params/first_three_years_instantaneous/locs_aachen.npy", locs)

# load data
average_10min = np.load("data/Pickles/Zugspitze/first_three_years/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/first_three_years/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/first_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/first_three_years/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/first_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/first_three_years_instantaneous/cs_zugspitze.npy", cs)
np.save("data/weibull_params/first_three_years_instantaneous/scales_zugspitze.npy", scales)
np.save("data/weibull_params/first_three_years_instantaneous/locs_zugspitze.npy", locs)

# load data
average_10min = np.load("data/Pickles/Boltenhagen/first_three_years/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/first_three_years/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/first_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/first_three_years/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/first_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/first_three_years_instantaneous/cs_boltenhagen.npy", cs)
np.save("data/weibull_params/first_three_years_instantaneous/scales_boltenhagen.npy", scales)
np.save("data/weibull_params/first_three_years_instantaneous/locs_boltenhagen.npy", locs)
# load data
average_10min = np.load("data/Pickles/Fichtelberg/first_three_years/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/first_three_years/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/first_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/first_three_years/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/first_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/first_three_years_instantaneous/cs_fichtelberg.npy", cs)
np.save("data/weibull_params/first_three_years_instantaneous/scales_fichtelberg.npy", scales)
np.save("data/weibull_params/first_three_years_instantaneous/locs_fichtelberg.npy", locs)


# load data
average_10min = np.load("data/Pickles/Aachen/last_three_years/average_10min.npy")
day = np.load("data/Pickles/Aachen/last_three_years/day.npy")
six_hour = np.load("data/Pickles/Aachen/last_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/last_three_years/three_hour.npy")
hour = np.load("data/Pickles/Aachen/last_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/last_three_years_instantaneous/cs_aachen.npy", cs)
np.save("data/weibull_params/last_three_years_instantaneous/scales_aachen.npy", scales)
np.save("data/weibull_params/last_three_years_instantaneous/locs_aachen.npy", locs)

# load data
average_10min = np.load("data/Pickles/Zugspitze/last_three_years/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/last_three_years/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/last_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/last_three_years/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/last_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/last_three_years_instantaneous/cs_zugspitze.npy", cs)
np.save("data/weibull_params/last_three_years_instantaneous/scales_zugspitze.npy", scales)
np.save("data/weibull_params/last_three_years_instantaneous/locs_zugspitze.npy", locs)

# load data
average_10min = np.load("data/Pickles/Boltenhagen/last_three_years/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/last_three_years/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/last_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/last_three_years/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/last_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/last_three_years_instantaneous/cs_boltenhagen.npy", cs)
np.save("data/weibull_params/last_three_years_instantaneous/scales_boltenhagen.npy", scales)
np.save("data/weibull_params/last_three_years_instantaneous/locs_boltenhagen.npy", locs)
# load data
average_10min = np.load("data/Pickles/Fichtelberg/last_three_years/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/last_three_years/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/last_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/last_three_years/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/last_three_years/hour.npy")

cs, locs, scales = weibull_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/weibull_params/last_three_years_instantaneous/cs_fichtelberg.npy", cs)
np.save("data/weibull_params/last_three_years_instantaneous/scales_fichtelberg.npy", scales)
np.save("data/weibull_params/last_three_years_instantaneous/locs_fichtelberg.npy", locs)
