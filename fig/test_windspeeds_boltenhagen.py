import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from src.windspeed_averages_wp import compute_windpower_generation
from windspeed_averages_wp import compute_average_windspeeds, drop_nans_DWD, set_date_DWD

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
data1 = data[(data["date"].dt.year.isin((int(2011), int(2012), int(2013))))]
data2 = data[(data["date"].dt.year.isin((int(2006), int(2007), int(2008))))]

fig, ax = plt.subplots(2, 3, sharex="col")
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data1, windspeeds="FF_10")
ax[0, 0].plot(average_10min.values)
(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily.values, average_hourly.values, average_10min.values
)
ax[0, 2].plot(np.cumsum(ten_min))
print(np.average(average_10min.values))
r = pd.Series(average_10min)
sns.kdeplot(ax=ax[0, 1], data=r, label="10min", linewidth=1)
(
    average_daily,
    average_hourly,
    average_10min,
    average_monthly,
) = compute_average_windspeeds(data2, windspeeds="FF_10")
(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily.values, average_hourly.values, average_10min.values
)
ax[1, 2].plot(np.cumsum(ten_min))
ax[1, 0].plot(average_10min.values)
print(np.average(average_10min.values))

r = pd.Series(average_10min)
sns.kdeplot(ax=ax[1, 1], data=r, label="10min", linewidth=1)
ax[1, 1].grid()
ax[0, 1].grid()

plt.show()
