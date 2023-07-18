import numpy as np
import pandas as pd
from src.kolmogorov_smirnov import kolmogorov_smirnov_multi

# load data
average_daily = np.load("data/Pickles/Penmanshiel/average_daily.npy")
average_hourly = np.load("data/Pickles/Penmanshiel/average_hourly.npy")
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
average_monthly = np.load("data/Pickles/Penmanshiel/average_monthly.npy")
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
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0554, p-value=0.0011208858258899156
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0640, p-value=2.9412287479179675e-05
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0737, p-value=1.4033944775031322e-07
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0554, p-value=0.0011208858258899156
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0136, p-value=0.44140531074658806
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0287, p-value=0.00011376687581897212
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0640, p-value=2.9412287479179675e-05
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0136, p-value=0.44140531074658806
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0159, p-value=0.005833941792182376
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0737, p-value=1.4033944775031322e-07
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0287, p-value=0.00011376687581897212
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0159, p-value=0.005833941792182376
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
 """
# load data
average_10min = np.load("data/Pickles/Penmanshiel/average_10min.npy")
day = np.load("data/Pickles/Penmanshiel/day.npy")
six_hour = np.load("data/Pickles/Penmanshiel/six_hour.npy")
three_hour = np.load("data/Pickles/Penmanshiel/three_hour.npy")
hour = np.load("data/Pickles/Penmanshiel/hour.npy")

data = [day, six_hour, three_hour, average_10min]
labels = ["daily", "six hourly", "three hourly", "10min"]
# plot_cumulative_densities(data, labels, "plots/open-source/Penmanshiel/1/cumulative_densities")
data = [
    pd.Series(day),
    pd.Series(six_hour),
    pd.Series(three_hour),
    pd.Series(average_10min),
]

kolmogorov_smirnov_multi(data, labels)

"""
 Kolmogorov-Smirnov Test ('daily', 'daily'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('daily', 'six hourly'): statistic=0.0414, p-value=0.030308244420341746
 Kolmogorov-Smirnov Test ('daily', 'three hourly'): statistic=0.0404, p-value=0.023449294103261256
 Kolmogorov-Smirnov Test ('daily', '10min'): statistic=0.0433, p-value=0.00662730556122448
 Kolmogorov-Smirnov Test ('six hourly', 'daily'): statistic=0.0414, p-value=0.030308244420341746
 Kolmogorov-Smirnov Test ('six hourly', 'six hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('six hourly', 'three hourly'): statistic=0.0052, p-value=0.9998945826437089
 Kolmogorov-Smirnov Test ('six hourly', '10min'): statistic=0.0066, p-value=0.9584901522496813
 Kolmogorov-Smirnov Test ('three hourly', 'daily'): statistic=0.0404, p-value=0.023449294103261256
 Kolmogorov-Smirnov Test ('three hourly', 'six hourly'): statistic=0.0052, p-value=0.9998945826437089
 Kolmogorov-Smirnov Test ('three hourly', 'three hourly'): statistic=0.0000, p-value=1.0
 Kolmogorov-Smirnov Test ('three hourly', '10min'): statistic=0.0059, p-value=0.8072232352309688
 Kolmogorov-Smirnov Test ('10min', 'daily'): statistic=0.0433, p-value=0.00662730556122448
 Kolmogorov-Smirnov Test ('10min', 'six hourly'): statistic=0.0066, p-value=0.9584901522496813
 Kolmogorov-Smirnov Test ('10min', 'three hourly'): statistic=0.0059, p-value=0.8072232352309688
 Kolmogorov-Smirnov Test ('10min', '10min'): statistic=0.0000, p-value=1.0
"""
