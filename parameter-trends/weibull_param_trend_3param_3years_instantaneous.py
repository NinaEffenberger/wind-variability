import numpy as np
from distributions import weibull_paramsdef_instanteous

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
