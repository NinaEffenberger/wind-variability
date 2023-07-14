import numpy as np
from distributions import gamma_paramsdef

# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/gamma_params/3_param/cs_kelmarsh.npy", cs)
np.save("data/gamma_params/3_param/scales_kelmarsh.npy", scales)
np.save("data/gamma_params/3_param/locs_kelmarsh.npy", locs)


# load data
average_daily = np.load("data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("data/Pickles/Penmanshiel/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly, average_daily, average_six_hourly, average_three_hourly, average_hourly, average_10min
)

np.save("data/gamma_params/3_param/cs_penmanshiel.npy", cs)
np.save("data/gamma_params/3_param/scales_penmanshiel.npy", scales)
np.save("data/gamma_params/3_param/locs_penmanshiel.npy", locs)


# load data
average_daily = np.load("data/Pickles/NWTC/average_daily.npy")
average_hourly = np.load("data/Pickles/NWTC/average_hourly.npy")
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
average_monthly = np.load("data/Pickles/NWTC/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)
np.save("data/gamma_params/3_param/cs_nwtc5.npy", cs)
np.save("data/gamma_params/3_param/scales_nwtc5.npy", scales)
np.save("data/gamma_params/3_param/locs_nwtc5.npy", locs)


# load data
average_daily = np.load("data/Pickles/Owez/average_daily.npy")
average_hourly = np.load("data/Pickles/Owez/average_hourly.npy")
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
average_monthly = np.load("data/Pickles/Owez/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)


cs, locs, scales = gamma_paramsdef(
    average_monthly, average_daily, average_six_hourly, average_three_hourly, average_hourly, average_10min
)

np.save("data/gamma_params/3_param/cs_owez.npy", cs)
np.save("data/gamma_params/3_param/scales_owez.npy", scales)
np.save("data/gamma_params/3_param/locs_owez.npy", locs)


# load data
average_daily = np.load("data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/gamma_params/3_param/cs_aachen.npy", cs)
np.save("data/gamma_params/3_param/scales_aachen.npy", scales)
np.save("data/gamma_params/3_param/locs_aachen.npy", locs)


# load data
average_daily = np.load("data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/gamma_params/3_param/cs_zugspitze.npy", cs)
np.save("data/gamma_params/3_param/scales_zugspitze.npy", scales)
np.save("data/gamma_params/3_param/locs_zugspitze.npy", locs)

# load data
average_daily = np.load("data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)
np.save("data/gamma_params/3_param/cs_boltenhagen.npy", cs)
np.save("data/gamma_params/3_param/scales_boltenhagen.npy", scales)
np.save("data/gamma_params/3_param/locs_boltenhagen.npy", locs)

# load data
average_daily = np.load("data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

cs, locs, scales = gamma_paramsdef(
    average_monthly,
    average_daily,
    average_six_hourly,
    average_three_hourly,
    average_hourly,
    average_10min,
)

np.save("data/gamma_params/3_param/cs_fichtelberg.npy", cs)
np.save("data/gamma_params/3_param/scales_fichtelberg.npy", scales)
np.save("data/gamma_params/3_param/locs_fichtelberg.npy", locs)
