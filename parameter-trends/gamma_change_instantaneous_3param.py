import numpy as np

from distributions import gamma_paramsdef_instanteous

# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_kelmarsh.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_kelmarsh.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_kelmarsh.npy", locs)

# load data
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_penmanshiel.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_penmanshiel.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_penmanshiel.npy", locs)

# load data
average_10min = np.load("data/Pickles/NWTC/average_10min.npy")
day = np.load("data/Pickles/NWTC/day.npy")
six_hour = np.load("data/Pickles/NWTC/six_hour.npy")
three_hour = np.load("data/Pickles/NWTC/three_hour.npy")
hour = np.load("data/Pickles/NWTC/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_nwtc5.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_nwtc5.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_nwtc5.npy", locs)

# load data
average_10min = np.load("data/Pickles/Owez/average_10min.npy")
day = np.load("data/Pickles/Owez/day.npy")
six_hour = np.load("data/Pickles/Owez/six_hour.npy")
three_hour = np.load("data/Pickles/Owez/three_hour.npy")
hour = np.load("data/Pickles/Owez/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_owez.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_owez.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_owez.npy", locs)

# load data
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
day = np.load("data/Pickles/Aachen/day.npy")
six_hour = np.load("data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/three_hour.npy")
hour = np.load("data/Pickles/Aachen/hour.npy")
cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)


np.save("data/gamma_params/3_param_instantaneous/cs_aachen.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_aachen.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_aachen.npy", locs)


# load data
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")
cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_zugspitze.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_zugspitze.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_zugspitze.npy", locs)


# load data
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
day = np.load("data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)
np.save("data/gamma_params/3_param_instantaneous/cs_boltenhagen.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_boltenhagen.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_boltenhagen.npy", locs)


# load data
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
day = np.load("data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/hour.npy")

cs, locs, scales = gamma_paramsdef_instanteous(
    day,
    six_hour,
    three_hour,
    hour,
    average_10min,
)

np.save("data/gamma_params/3_param_instantaneous/cs_fichtelberg.npy", cs)
np.save("data/gamma_params/3_param_instantaneous/scales_fichtelberg.npy", scales)
np.save("data/gamma_params/3_param_instantaneous/locs_fichtelberg.npy", locs)
