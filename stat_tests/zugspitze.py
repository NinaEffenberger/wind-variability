import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import (kolmogorov_smirnov_multi,
                                plot_cumulative_densities_day)
from windspeed_averages_wp import (compute_average_windspeeds, drop_nans,
                                   load_data, set_date)

# load data
average_daily = np.load("data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0474, p-value=1.3201828044471578e-18
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0543, p-value=1.5714374978140025e-20
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0877, p-value=1.4049505656653178e-28
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0474, p-value=1.3201828044471578e-18
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0146, p-value=0.04180459868467612
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0352, p-value=2.561394885090579e-06
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0543, p-value=1.5714374978140025e-20
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0146, p-value=0.04180459868467612
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0215, p-value=0.04968013302229445
 """
# load data
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0268, p-value=0.9920106805050907
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0424, p-value=0.7141027560747789
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1355, p-value=2.2246743328152025e-05
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0268, p-value=0.9920106805050907
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0226, p-value=0.9985717616877197
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0413, p-value=0.6333629830201767
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0424, p-value=0.7141027560747789
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0226, p-value=0.9985717616877197
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0237, p-value=0.9914081639357595
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1355, p-value=2.2246743328152025e-05
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0413, p-value=0.6333629830201767
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0237, p-value=0.9914081639357595
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
