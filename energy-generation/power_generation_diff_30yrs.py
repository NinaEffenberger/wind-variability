import numpy as np
from src.windspeed_averages_wp import compute_windpower_generation, compute_windpower_generation_instantaneous

# load data
average_daily = np.load("data/Pickles/Aachen/average_daily.npy")
average_hourly = np.load("data/Pickles/Aachen/average_hourly.npy")
average_10min = np.load("data/Pickles/Aachen/average_10min.npy")
average_monthly = np.load("data/Pickles/Aachen/average_monthly.npy")
day = np.load("data/Pickles/Aachen/day.npy")
six_hour = np.load("data/Pickles/Aachen/six_hour.npy")
three_hour = np.load("data/Pickles/Aachen/three_hour.npy")
hour = np.load("data/Pickles/Aachen/hour.npy")
days = np.load("data/Pickles/Aachen/days.npy", allow_pickle=True)

(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily, average_hourly, average_10min
)
(
    hourly_winds,
    three_hourly_winds,
    daily_winds,
    ten_min_winds,
    six_hourly_winds,
) = compute_windpower_generation_instantaneous(day, six_hour, three_hour, hour, average_10min)

np.save("data/power-gen/Aachen/daily_avrg.npy", daily)
np.save("data/power-gen/Aachen/six_hourly_avrg.npy", six_hourly)
np.save("data/power-gen/Aachen/three_hourly_avrg.npy", three_hourly)
np.save("data/power-gen/Aachen/ten_min.npy", ten_min)
np.save("data/power-gen/Aachen/daily_inst.npy", daily_winds)
np.save("data/power-gen/Aachen/six_hourly_inst.npy", six_hourly_winds)
np.save("data/power-gen/Aachen/three_hourly_inst.npy", three_hourly_winds)
np.save("data/power-gen/Aachen/days.npy", days)

# load data
average_daily = np.load("data/Pickles/Fichtelberg/average_daily.npy")
average_hourly = np.load("data/Pickles/Fichtelberg/average_hourly.npy")
average_10min = np.load("data/Pickles/Fichtelberg/average_10min.npy")
average_monthly = np.load("data/Pickles/Fichtelberg/average_monthly.npy")
day = np.load("data/Pickles/Fichtelberg/day.npy")
six_hour = np.load("data/Pickles/Fichtelberg/six_hour.npy")
three_hour = np.load("data/Pickles/Fichtelberg/three_hour.npy")
hour = np.load("data/Pickles/Fichtelberg/hour.npy")
days = np.load("data/Pickles/Fichtelberg/days.npy", allow_pickle=True)

(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily, average_hourly, average_10min
)
(
    hourly_winds,
    three_hourly_winds,
    daily_winds,
    ten_min_winds,
    six_hourly_winds,
) = compute_windpower_generation_instantaneous(day, six_hour, three_hour, hour, average_10min)

np.save("data/power-gen/Fichtelberg/daily_avrg.npy", daily)
np.save("data/power-gen/Fichtelberg/six_hourly_avrg.npy", six_hourly)
np.save("data/power-gen/Fichtelberg/three_hourly_avrg.npy", three_hourly)
np.save("data/power-gen/Fichtelberg/ten_min.npy", ten_min)
np.save("data/power-gen/Fichtelberg/daily_inst.npy", daily_winds)
np.save("data/power-gen/Fichtelberg/six_hourly_inst.npy", six_hourly_winds)
np.save("data/power-gen/Fichtelberg/three_hourly_inst.npy", three_hourly_winds)
np.save("data/power-gen/Fichtelberg/days.npy", days)

# load data
average_daily = np.load("data/Pickles/Boltenhagen/average_daily.npy")
average_hourly = np.load("data/Pickles/Boltenhagen/average_hourly.npy")
average_10min = np.load("data/Pickles/Boltenhagen/average_10min.npy")
average_monthly = np.load("data/Pickles/Boltenhagen/average_monthly.npy")
day = np.load("data/Pickles/Boltenhagen/day.npy")
six_hour = np.load("data/Pickles/Boltenhagen/six_hour.npy")
three_hour = np.load("data/Pickles/Boltenhagen/three_hour.npy")
hour = np.load("data/Pickles/Boltenhagen/hour.npy")
days = np.load("data/Pickles/Boltenhagen/days.npy", allow_pickle=True)

(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily, average_hourly, average_10min
)
(
    hourly_winds,
    three_hourly_winds,
    daily_winds,
    ten_min_winds,
    six_hourly_winds,
) = compute_windpower_generation_instantaneous(day, six_hour, three_hour, hour, average_10min)

np.save("data/power-gen/Boltenhagen/daily_avrg.npy", daily)
np.save("data/power-gen/Boltenhagen/six_hourly_avrg.npy", six_hourly)
np.save("data/power-gen/Boltenhagen/three_hourly_avrg.npy", three_hourly)
np.save("data/power-gen/Boltenhagen/ten_min.npy", ten_min)
np.save("data/power-gen/Boltenhagen/daily_inst.npy", daily_winds)
np.save("data/power-gen/Boltenhagen/six_hourly_inst.npy", six_hourly_winds)
np.save("data/power-gen/Boltenhagen/three_hourly_inst.npy", three_hourly_winds)
np.save("data/power-gen/Boltenhagen/days.npy", days)

# load data
average_daily = np.load("data/Pickles/Zugspitze/average_daily.npy")
average_hourly = np.load("data/Pickles/Zugspitze/average_hourly.npy")
average_10min = np.load("data/Pickles/Zugspitze/average_10min.npy")
average_monthly = np.load("data/Pickles/Zugspitze/average_monthly.npy")
day = np.load("data/Pickles/Zugspitze/day.npy")
six_hour = np.load("data/Pickles/Zugspitze/six_hour.npy")
three_hour = np.load("data/Pickles/Zugspitze/three_hour.npy")
hour = np.load("data/Pickles/Zugspitze/hour.npy")
days = np.load("data/Pickles/Zugspitze/days.npy", allow_pickle=True)

(daily, six_hourly, three_hourly, hourly, ten_min) = compute_windpower_generation(
    average_daily, average_hourly, average_10min
)
(
    hourly_winds,
    three_hourly_winds,
    daily_winds,
    ten_min_winds,
    six_hourly_winds,
) = compute_windpower_generation_instantaneous(day, six_hour, three_hour, hour, average_10min)

np.save("data/power-gen/Zugspitze/daily_avrg.npy", daily)
np.save("data/power-gen/Zugspitze/six_hourly_avrg.npy", six_hourly)
np.save("data/power-gen/Zugspitze/three_hourly_avrg.npy", three_hourly)
np.save("data/power-gen/Zugspitze/ten_min.npy", ten_min)
np.save("data/power-gen/Zugspitze/daily_inst.npy", daily_winds)
np.save("data/power-gen/Zugspitze/six_hourly_inst.npy", six_hourly_winds)
np.save("data/power-gen/Zugspitze/three_hourly_inst.npy", three_hourly_winds)
np.save("data/power-gen/Zugspitze/days.npy", days)
