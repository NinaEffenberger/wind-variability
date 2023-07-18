import numpy as np
import pandas as pd
from distributions import compute_instantenous_windspeeds
from kolmogorov_smirnov import (kolmogorov_smirnov_multi,
                                plot_cumulative_densities_day)
from windspeed_averages_wp import (compute_average_windspeeds, drop_nans,
                                   load_data, set_date)

# load data
average_daily = np.load("data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0373, p-value=1.4468682194247115e-06
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0453, p-value=4.933877981561849e-08
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0854, p-value=1.5364837696092953e-15
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0373, p-value=1.4468682194247115e-06
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0102, p-value=0.704951820112725
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0315, p-value=0.006870229684123575
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0453, p-value=4.933877981561849e-08
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0102, p-value=0.704951820112725
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0273, p-value=0.09131004470449959
 """
# load data
average_10min = np.load("data/Pickles/Aachen/first_three_years/average_10min.npy")
day = np.load("data/Pickles/Aachen/first_three_years/day.npy")
six_hour = np.load("data/Pickles/Aachen/first_three_years/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/first_three_years/three_hour.npy")
hour = np.load("data/Pickles/Aachen/first_three_years/hour.npy")

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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0391, p-value=0.9900151940334373
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0308, p-value=0.9997030667215446
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.1395, p-value=0.006516551541099631
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0391, p-value=0.9900151940334373
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0144, p-value=0.9999999999999998
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.1154, p-value=0.03132700885763083
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0308, p-value=0.9997030667215446
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0144, p-value=0.9999999999999998
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0506, p-value=0.8135166498040465
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.1395, p-value=0.006516551541099631
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.1154, p-value=0.03132700885763083
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0506, p-value=0.8135166498040465
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
