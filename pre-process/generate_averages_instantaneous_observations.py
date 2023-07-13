import glob
import os

import numpy as np
import pandas as pd
import xarray as xr
from distributions import compute_instantenous_windspeeds
from windspeed_averages_wp import (
    compute_average_windspeeds,
    drop_nans,
    drop_nans_DWD,
    load_data,
    set_date,
    set_date_DWD,
)

"""
# load data
paths = [
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2016-01-03_-_2017-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2017-01-01_-_2018-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2018-01-01_-_2019-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2019-01-01_-_2020-01-01_228.csv",
    "data/Kelmarsh/Turbine_Data_Kelmarsh_1_2020-01-01_-_2021-01-01_228.csv",
]
data = load_data(paths)
set_date(data, current_name="Date and time")
average_daily = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)", only_daily=True)
data = drop_nans(data, average_daily)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)")
np.save("data/Pickles/Kelmarsh/average_daily.npy", average_daily)
np.save("data/Pickles/Kelmarsh/average_hourly.npy", average_hourly)
np.save("data/Pickles/Kelmarsh/average_10min.npy", average_10min)
np.save("data/Pickles/Kelmarsh/average_monthly.npy", average_monthly)
np.save("data/Pickles/Kelmarsh/day.npy", day)
np.save("data/Pickles/Kelmarsh/six_hour.npy", six_hour)
np.save("data/Pickles/Kelmarsh/three_hour.npy", three_hour)
np.save("data/Pickles/Kelmarsh/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Kelmarsh/days.npy", days)


# load data
paths = [
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2016-07-19_-_2017-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2017-01-01_-_2018-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2018-01-01_-_2019-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2019-01-01_-_2020-01-01_1051.csv",
    "data/Penmanshiel/Turbine_Data_Penmanshiel_11_2020-01-01_-_2021-01-01_1051.csv",
]
data = load_data(paths)
set_date(data, current_name="Date and time")
average_daily = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)", only_daily=True)
data = drop_nans(data, average_daily)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="Wind speed (m/s)")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="Wind speed (m/s)")
np.save("data/Pickles/Penmanshiel/average_daily.npy", average_daily)
np.save("data/Pickles/Penmanshiel/average_hourly.npy", average_hourly)
np.save("data/Pickles/Penmanshiel/average_10min.npy", average_10min)
np.save("data/Pickles/Penmanshiel/average_monthly.npy", average_monthly)
np.save("data/Pickles/Penmanshiel/day.npy", day)
np.save("data/Pickles/Penmanshiel/six_hour.npy", six_hour)
np.save("data/Pickles/Penmanshiel/three_hour.npy", three_hour)
np.save("data/Pickles/Penmanshiel/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Penmanshiel/days.npy", days)

# load data
path = "data/tall_tower/nwtc_m5/huragl87S1/windagl87S1"
files = glob.glob(os.path.join(path, "*.nc"))

data = None
for f in files:
    # initialize dataframe
    if not isinstance(data, pd.DataFrame):
        ds = xr.open_dataset(f)
        data = ds.to_dataframe()
        data["date"] = data.index.get_level_values(0)
        data.set_index(["date"])
        average_daily = compute_average_windspeeds(data, windspeeds="windagl87S1", only_daily=True)
        data = drop_nans(data, average_daily)
    else:
        ds = xr.open_dataset(f)
        filedata = ds.to_dataframe()
        filedata["date"] = filedata.index.get_level_values(0)
        filedata.set_index(["date"])
        average_daily = compute_average_windspeeds(filedata, windspeeds="windagl87S1", only_daily=True)
        filedata = drop_nans(filedata, average_daily)
        data = pd.concat([data, filedata])


# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="windagl87S1")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="windagl87S1")
np.save("data/Pickles/NWTC/average_daily.npy", average_daily)
np.save("data/Pickles/NWTC/average_hourly.npy", average_hourly)
np.save("data/Pickles/NWTC/average_10min.npy", average_10min)
np.save("data/Pickles/NWTC/average_monthly.npy", average_monthly)
np.save("data/Pickles/NWTC/day.npy", day)
np.save("data/Pickles/NWTC/six_hour.npy", six_hour)
np.save("data/Pickles/NWTC/three_hour.npy", three_hour)
np.save("data/Pickles/NWTC/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/NWTC/days.npy", days)

# load data
path = "data/tall_tower/oweg/windagl116S1"
files = glob.glob(os.path.join(path, "*.nc"))

data = None
for f in files:
    # initialize dataframe
    if not isinstance(data, pd.DataFrame):
        ds = xr.open_dataset(f)
        data = ds.to_dataframe()
        data["date"] = data.index.get_level_values(0)
        data.set_index(["date"])
        average_daily = compute_average_windspeeds(data, windspeeds="windagl116S1", only_daily=True)
        data = drop_nans(data, average_daily)
    else:
        ds = xr.open_dataset(f)
        filedata = ds.to_dataframe()
        filedata["date"] = filedata.index.get_level_values(0)
        filedata.set_index(["date"])
        average_daily = compute_average_windspeeds(filedata, windspeeds="windagl116S1", only_daily=True)
        filedata = drop_nans(filedata, average_daily)
        data = pd.concat([data, filedata])


# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="windagl116S1")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="windagl116S1")

np.save("data/Pickles/Owez/average_daily.npy", average_daily)
np.save("data/Pickles/Owez/average_hourly.npy", average_hourly)
np.save("data/Pickles/Owez/average_10min.npy", average_10min)
np.save("data/Pickles/Owez/average_monthly.npy", average_monthly)
np.save("data/Pickles/Owez/day.npy", day)
np.save("data/Pickles/Owez/six_hour.npy", six_hour)
np.save("data/Pickles/Owez/three_hour.npy", three_hour)
np.save("data/Pickles/Owez/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Owez/days.npy", days)

# load data
data1 = pd.read_table(
    "data/DWD/Aachen_003/produkt_zehn_min_ff_19930429_19991231_00003.txt",
    header=0,
    sep=";",
)
data2 = pd.read_table(
    "data/DWD/Aachen_003/produkt_zehn_min_ff_20000101_20091231_00003.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "data/DWD/Aachen_003/produkt_zehn_min_ff_20100101_20110331_00003.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3])
set_date_DWD(data)
data = drop_nans_DWD(data)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Aachen/average_daily.npy", average_daily)
np.save("data/Pickles/Aachen/average_hourly.npy", average_hourly)
np.save("data/Pickles/Aachen/average_10min.npy", average_10min)
np.save("data/Pickles/Aachen/average_monthly.npy", average_monthly)
np.save("data/Pickles/Aachen/day.npy", day)
np.save("data/Pickles/Aachen/six_hour.npy", six_hour)
np.save("data/Pickles/Aachen/three_hour.npy", three_hour)
np.save("data/Pickles/Aachen/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Aachen/days.npy", days)

# load data
data1 = pd.read_table(
    "data/DWD/Zugspitze_5792/produkt_zehn_min_ff_19940731_19991231_05792.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "data/DWD/Zugspitze_5792/produkt_zehn_min_ff_20000101_20091231_05792.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "data/DWD/Zugspitze_5792/produkt_zehn_min_ff_20100101_20191231_05792.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "data/DWD/Zugspitze_5792/produkt_zehn_min_ff_20200101_20221231_05792.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)
# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Zugspitze/average_daily.npy", average_daily)
np.save("data/Pickles/Zugspitze/average_hourly.npy", average_hourly)
np.save("data/Pickles/Zugspitze/average_10min.npy", average_10min)
np.save("data/Pickles/Zugspitze/average_monthly.npy", average_monthly)
np.save("data/Pickles/Zugspitze/day.npy", day)
np.save("data/Pickles/Zugspitze/six_hour.npy", six_hour)
np.save("data/Pickles/Zugspitze/three_hour.npy", three_hour)
np.save("data/Pickles/Zugspitze/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Zugspitze/days.npy", days)

# load data
data1 = pd.read_table(
    "data/DWD/Boltenhagen/produkt_zehn_min_ff_19911107_19991231_00596.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "data/DWD/Boltenhagen/produkt_zehn_min_ff_20000101_20091231_00596.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "data/DWD/Boltenhagen/produkt_zehn_min_ff_20100101_20191231_00596.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "data/DWD/Boltenhagen/produkt_zehn_min_ff_20200101_20221231_00596.txt",
    header=0,
    sep=";",
)
data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Boltenhagen/average_daily.npy", average_daily)
np.save("data/Pickles/Boltenhagen/average_hourly.npy", average_hourly)
np.save("data/Pickles/Boltenhagen/average_10min.npy", average_10min)
np.save("data/Pickles/Boltenhagen/average_monthly.npy", average_monthly)
np.save("data/Pickles/Boltenhagen/day.npy", day)
np.save("data/Pickles/Boltenhagen/six_hour.npy", six_hour)
np.save("data/Pickles/Boltenhagen/three_hour.npy", three_hour)
np.save("data/Pickles/Boltenhagen/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Boltenhagen/days.npy", days)
"""
# load data
data1 = pd.read_table(
    "data/DWD/Fichtelberg/produkt_zehn_min_ff_19931216_19991231_01357.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "data/DWD/Fichtelberg/produkt_zehn_min_ff_20000101_20091231_01357.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "data/DWD/Fichtelberg/produkt_zehn_min_ff_20100101_20191231_01357.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "data/DWD/Fichtelberg/produkt_zehn_min_ff_20200101_20221231_01357.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)

# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Fichtelberg/average_daily.npy", average_daily)
np.save("data/Pickles/Fichtelberg/average_hourly.npy", average_hourly)
np.save("data/Pickles/Fichtelberg/average_10min.npy", average_10min)
np.save("data/Pickles/Fichtelberg/average_monthly.npy", average_monthly)
np.save("data/Pickles/Fichtelberg/day.npy", day)
np.save("data/Pickles/Fichtelberg/six_hour.npy", six_hour)
np.save("data/Pickles/Fichtelberg/three_hour.npy", three_hour)
np.save("data/Pickles/Fichtelberg/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Fichtelberg/days.npy", days)
