import numpy as np
from src.distributions import weibull_paramsdef

# load data
average_daily = np.load("data/Pickles/Aachen/first_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/first_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/first_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/first_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/first_three_years/cs_aachen.npy", cs)
np.save("data/weibull_params/first_three_years/scales_aachen.npy", scales)
np.save("data/weibull_params/first_three_years/locs_aachen.npy", locs)


# load data
average_daily = np.load("data/Pickles/Zugspitze/first_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/first_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/first_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/first_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/first_three_years/cs_zugspitze.npy", cs)
np.save("data/weibull_params/first_three_years/scales_zugspitze.npy", scales)
np.save("data/weibull_params/first_three_years/locs_zugspitze.npy", locs)

# load data
average_daily = np.load("data/Pickles/Boltenhagen/first_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/first_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/first_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/first_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/first_three_years/cs_boltenhagen.npy", cs)
np.save("data/weibull_params/first_three_years/scales_boltenhagen.npy", scales)
np.save("data/weibull_params/first_three_years/locs_boltenhagen.npy", locs)

# load data
average_daily = np.load("data/Pickles/Fichtelberg/first_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/first_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/first_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/first_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/first_three_years/cs_fichtelberg.npy", cs)
np.save("data/weibull_params/first_three_years/scales_fichtelberg.npy", scales)
np.save("data/weibull_params/first_three_years/locs_fichtelberg.npy", locs)

# load data
average_daily = np.load("data/Pickles/Aachen/last_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/last_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/last_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/last_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/last_three_years/cs_aachen.npy", cs)
np.save("data/weibull_params/last_three_years/scales_aachen.npy", scales)
np.save("data/weibull_params/last_three_years/locs_aachen.npy", locs)


# load data
average_daily = np.load("data/Pickles/Zugspitze/last_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/last_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/last_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/last_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/last_three_years/cs_zugspitze.npy", cs)
np.save("data/weibull_params/last_three_years/scales_zugspitze.npy", scales)
np.save("data/weibull_params/last_three_years/locs_zugspitze.npy", locs)

# load data
average_daily = np.load("data/Pickles/Boltenhagen/last_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/last_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/last_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/last_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/last_three_years/cs_boltenhagen.npy", cs)
np.save("data/weibull_params/last_three_years/scales_boltenhagen.npy", scales)
np.save("data/weibull_params/last_three_years/locs_boltenhagen.npy", locs)

# load data
average_daily = np.load("data/Pickles/Fichtelberg/last_three_years/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/last_three_years/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/last_three_years/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/last_three_years/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = weibull_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/weibull_params/last_three_years/cs_fichtelberg.npy", cs)
np.save("data/weibull_params/last_three_years/scales_fichtelberg.npy", scales)
np.save("data/weibull_params/last_three_years/locs_fichtelberg.npy", locs)
