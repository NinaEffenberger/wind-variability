import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import kolmogorov_smirnov_multi, plot_cumulative_densities_day
from windspeed_averages_wp import compute_average_windspeeds, drop_nans, load_data, set_date

# load data
average_daily = np.load("data/Pickles/Kelmarsh/average_daily.npy")
average_hourly = np.load("data/Pickles/Kelmarsh/average_hourly.npy")
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
average_monthly = np.load("data/Pickles/Kelmarsh/average_monthly.npy")
average_three_hourly = np.average(average_hourly.reshape(-1, 3), axis=1)
average_six_hourly = np.average(average_hourly.reshape(-1, 6), axis=1)

data = [
    average_daily,
    average_six_hourly.squeeze(),
    average_three_hourly.squeeze(),
    average_10min,
]

labels = ["daily", "six hourly", "three hourly", "10min"]
kolmogorov_smirnov_multi(data, labels)
"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0501, p-value=0.002240874322234314
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0597, p-value=4.303253005939263e-05
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0768, p-value=4.981704241920966e-09
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0501, p-value=0.002240874322234314
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0127, p-value=0.4542869728369602
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0309, p-value=6.880997304334042e-06
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0597, p-value=4.303253005939263e-05
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0127, p-value=0.4542869728369602
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0190, p-value=0.00018537178544951824
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0768, p-value=4.981704241920966e-09
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0309, p-value=6.880997304334042e-06
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0190, p-value=0.00018537178544951824
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
 """
# load data
average_10min = np.load("data/Pickles/Kelmarsh/average_10min.npy")
day = np.load("data/Pickles/Kelmarsh/day.npy")
six_hour = np.load("data/Pickles/Kelmarsh/six_hour.npy")
three_hour = np.load("data/Pickles/Kelmarsh/three_hour.npy")
hour = np.load("data/Pickles/Kelmarsh/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Kelmarsh/1/cumulative_densities")
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0424, p-value=0.01540315084157475
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0442, p-value=0.005579681435643059
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0451, p-value=0.002151136007649057
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0424, p-value=0.01540315084157475
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0045, p-value=0.9999849679947429
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0057, p-value=0.9812420250704019
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0442, p-value=0.005579681435643059
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0045, p-value=0.9999849679947429
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0028, p-value=0.9999498732045523
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0451, p-value=0.002151136007649057
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0057, p-value=0.9812420250704019
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0028, p-value=0.9999498732045523
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
