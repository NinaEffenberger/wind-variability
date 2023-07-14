import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from windspeed_averages_wp import compute_average_windspeeds, drop_nans_DWD, set_date_DWD

# load data
data1 = pd.read_table(
    "bigdata/DWD/Aachen_003/produkt_zehn_min_ff_19930429_19991231_00003.txt",
    header=0,
    sep=";",
)
data2 = pd.read_table(
    "bigdata/DWD/Aachen_003/produkt_zehn_min_ff_20000101_20091231_00003.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "bigdata/DWD/Aachen_003/produkt_zehn_min_ff_20100101_20110331_00003.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3])
set_date_DWD(data)
data = drop_nans_DWD(data)
data1 = data[(data["date"].dt.year.isin((int(1994), int(1995), int(1996))))]
data2 = data[(data["date"].dt.year.isin((int(2008), int(2009), int(2010))))]
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data1, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Aachen/first_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Aachen/first_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Aachen/first_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Aachen/first_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Aachen/first_three_years/day.npy", day)
np.save("data/Pickles/Aachen/first_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Aachen/first_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Aachen/first_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Aachen/first_three_years/days.npy", days)

(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data2, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Aachen/last_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Aachen/last_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Aachen/last_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Aachen/last_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Aachen/last_three_years/day.npy", day)
np.save("data/Pickles/Aachen/last_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Aachen/last_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Aachen/last_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Aachen/last_three_years/days.npy", days)


# load data
data1 = pd.read_table(
    "bigdata/DWD/Zugspitze_5792/produkt_zehn_min_ff_19940731_19991231_05792.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "bigdata/DWD/Zugspitze_5792/produkt_zehn_min_ff_20000101_20091231_05792.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "bigdata/DWD/Zugspitze_5792/produkt_zehn_min_ff_20100101_20191231_05792.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "bigdata/DWD/Zugspitze_5792/produkt_zehn_min_ff_20200101_20221231_05792.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)
data1 = data[(data["date"].dt.year.isin((int(1995), int(1996), int(1997))))]
data2 = data[(data["date"].dt.year.isin((int(2020), int(2021), int(2022))))]
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data1, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Zugspitze/first_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Zugspitze/first_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Zugspitze/first_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Zugspitze/first_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Zugspitze/first_three_years/day.npy", day)
np.save("data/Pickles/Zugspitze/first_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Zugspitze/first_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Zugspitze/first_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Zugspitze/first_three_years/days.npy", days)

(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data2, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Zugspitze/last_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Zugspitze/last_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Zugspitze/last_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Zugspitze/last_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Zugspitze/last_three_years/day.npy", day)
np.save("data/Pickles/Zugspitze/last_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Zugspitze/last_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Zugspitze/last_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Zugspitze/last_three_years/days.npy", days)

# load data
data1 = pd.read_table(
    "bigdata/DWD/Boltenhagen/produkt_zehn_min_ff_19911107_19991231_00596.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "bigdata/DWD/Boltenhagen/produkt_zehn_min_ff_20000101_20091231_00596.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "bigdata/DWD/Boltenhagen/produkt_zehn_min_ff_20100101_20191231_00596.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "bigdata/DWD/Boltenhagen/produkt_zehn_min_ff_20200101_20221231_00596.txt",
    header=0,
    sep=";",
)
data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)
data1 = data[(data["date"].dt.year.isin((int(1992), int(1993), int(1994))))]
data2 = data[(data["date"].dt.year.isin((int(2020), int(2021), int(2022))))]
# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data1, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Boltenhagen/first_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Boltenhagen/first_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Boltenhagen/first_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Boltenhagen/first_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Boltenhagen/first_three_years/day.npy", day)
np.save("data/Pickles/Boltenhagen/first_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Boltenhagen/first_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Boltenhagen/first_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Boltenhagen/first_three_years/days.npy", days)
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data2, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Boltenhagen/last_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Boltenhagen/last_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Boltenhagen/last_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Boltenhagen/last_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Boltenhagen/last_three_years/day.npy", day)
np.save("data/Pickles/Boltenhagen/last_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Boltenhagen/last_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Boltenhagen/last_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Boltenhagen/last_three_years/days.npy", days)


# load data
data1 = pd.read_table(
    "bigdata/DWD/Fichtelberg/produkt_zehn_min_ff_19931216_19991231_01357.txt",
    header=0,
    sep=";",
)

data2 = pd.read_table(
    "bigdata/DWD/Fichtelberg/produkt_zehn_min_ff_20000101_20091231_01357.txt",
    header=0,
    sep=";",
)
data3 = pd.read_table(
    "bigdata/DWD/Fichtelberg/produkt_zehn_min_ff_20100101_20191231_01357.txt",
    header=0,
    sep=";",
)
data4 = pd.read_table(
    "bigdata/DWD/Fichtelberg/produkt_zehn_min_ff_20200101_20221231_01357.txt",
    header=0,
    sep=";",
)

data = pd.concat([data1, data2, data3, data4])
set_date_DWD(data)
data = drop_nans_DWD(data)
data1 = data[(data["date"].dt.year.isin((int(1994), int(1995), int(1996))))]
data2 = data[(data["date"].dt.year.isin((int(2020), int(2021), int(2022))))]
# recompute and exclude nans
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data1, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Fichtelberg/first_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Fichtelberg/first_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Fichtelberg/first_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Fichtelberg/first_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Fichtelberg/first_three_years/day.npy", day)
np.save("data/Pickles/Fichtelberg/first_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Fichtelberg/first_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Fichtelberg/first_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Fichtelberg/first_three_years/days.npy", days)

(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data2, windspeeds="FF_10")

day, six_hour, three_hour, hour = compute_instantenous_windspeeds(data, windspeeds="FF_10")
np.save("data/Pickles/Fichtelberg/last_three_years/average_daily.npy", average_daily)
np.save("data/Pickles/Fichtelberg/last_three_years/average_hourly.npy", average_hourly)
np.save("data/Pickles/Fichtelberg/last_three_years/average_10min.npy", average_10min)
np.save("data/Pickles/Fichtelberg/last_three_years/average_monthly.npy", average_monthly)
np.save("data/Pickles/Fichtelberg/last_three_years/day.npy", day)
np.save("data/Pickles/Fichtelberg/last_three_years/six_hour.npy", six_hour)
np.save("data/Pickles/Fichtelberg/last_three_years/three_hour.npy", three_hour)
np.save("data/Pickles/Fichtelberg/last_three_years/hour.npy", hour)
days = average_daily.index.get_level_values(0)
np.save("data/Pickles/Fichtelberg/last_three_years/days.npy", days)
