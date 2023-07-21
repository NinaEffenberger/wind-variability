import numpy as np
import pandas as pd
import windpowerlib


def load_data(paths):
    data = pd.read_csv(paths[0])
    for i in range(len(paths) - 1):
        new_file = pd.read_csv(paths[1 + i])
        data = pd.concat([data, new_file], ignore_index=True)
    return data


def set_date(data, current_name="Date and time"):
    data["date"] = pd.to_datetime(data[current_name])
    data.set_index(["date"])


def compute_average_windspeeds(data, windspeeds="Wind speed (m/s)", only_daily=False):
    # work around as skipna is not supported by groupby
    average_daily = data[windspeeds].groupby(data["date"].dt.date).apply(lambda x: x.mean(skipna=False))
    if only_daily == False:
        average_hourly = (
            data[windspeeds].groupby([data["date"].dt.date, data["date"].dt.hour]).apply(lambda x: x.mean(skipna=False))
        )
        ten_min_windspeed = (
            data[windspeeds]
            .groupby([data["date"].dt.date, data["date"].dt.hour, data["date"].dt.minute])
            .apply(lambda x: x.mean(skipna=False))
        )
        monthly_windspeed = data.groupby(pd.PeriodIndex(data["date"], freq="M"))[windspeeds].mean()
        monthly_count = (data.groupby(pd.PeriodIndex(data["date"], freq="M"))[windspeeds].count() / 24 / 6).values
        monthly_count = [int(x) for x in monthly_count]
        monthly_windspeed = np.repeat(monthly_windspeed, monthly_count)
        # compute number of days per month for differnce plots
        return (
            average_daily,
            average_hourly,
            ten_min_windspeed,
            monthly_windspeed,
        )
    return average_daily


# this is not the correct turbine
def compute_windpower(weather):
    enercon_e126 = {
        "turbine_type": "E-92/2350",  # turbine type as in register
        "hub_height": 79,  # in m
    }
    e126 = windpowerlib.WindTurbine(**enercon_e126)
    mc_e126 = windpowerlib.ModelChain(e126)
    # write power output time series to WindTurbine object
    power = mc_e126.calculate_power_output(weather, 1)
    return power


# convenience function to print number of missing values
def print_missing_values(average_daily, average_hourly, ten_min_windspeed):
    print(average_daily.isnull().sum())
    print(average_hourly.isnull().sum())
    print(ten_min_windspeed.isnull().sum())


def drop_nans(data, average_daily):
    # days where values are missing
    nan_indices = np.where(average_daily.isna())[0]
    nan_days = average_daily.iloc[nan_indices].index

    # exclude all days where value are missing
    data = data.drop(data[data["date"].dt.date.isin(nan_days)].index)
    return data


def compute_windpower_generation(daily_windspeed, hourly_windspeed, ten_min_windspeed):
    daily = compute_windpower(daily_windspeed) * 1e-6
    six_hour = np.average(hourly_windspeed.reshape(-1, 6), axis=1)
    three_hour = np.average(hourly_windspeed.reshape(-1, 3), axis=1)
    six_hour = np.average(compute_windpower(six_hour).reshape(-1, 4), axis=1) * 1e-6
    three_hour = np.average(compute_windpower(three_hour).reshape(-1, 8), axis=1) * 1e-6
    hour = np.average(compute_windpower(hourly_windspeed).reshape(-1, 24), axis=1) * 1e-6
    ten_min = np.average(compute_windpower(ten_min_windspeed).reshape(-1, 24 * 6), axis=1) * 1e-6
    return daily, six_hour, three_hour, hour, ten_min


def compute_windpower_generation_cmip(daily_windspeed, six_hour_avrg, three_hour_avrg, six_hour_inst, three_hour_inst):
    daily = compute_windpower(daily_windspeed) * 1e-6
    six_hour_avrg = np.average(compute_windpower(six_hour_avrg).reshape(-1, 4), axis=1) * 1e-6
    six_hour_inst = np.average(compute_windpower(six_hour_inst).reshape(-1, 4), axis=1) * 1e-6
    three_hour_inst = np.average(compute_windpower(three_hour_inst).reshape(-1, 8), axis=1) * 1e-6
    three_hour_avrg = np.average(compute_windpower(three_hour_avrg).reshape(-1, 8), axis=1) * 1e-6
    return daily, six_hour_avrg, three_hour_avrg, six_hour_inst, three_hour_inst


def compute_windpower_generation_instantaneous(
    daily_windspeed, six_hourly, three_hourly, hourly_windspeed, ten_min_windspeed
):
    hourly_winds = np.average(compute_windpower(hourly_windspeed).reshape(-1, 24), axis=1) * 1e-6
    six_hourly_winds = np.average(compute_windpower(six_hourly).reshape(-1, 4), axis=1) * 1e-6
    three_hourly_winds = np.average(compute_windpower(three_hourly).reshape(-1, 8), axis=1) * 1e-6
    daily_winds = compute_windpower(daily_windspeed) * 1e-6
    ten_min_winds = np.average(compute_windpower(ten_min_windspeed).reshape(-1, 144), axis=1) * 1e-6
    return (
        hourly_winds,
        three_hourly_winds,
        daily_winds,
        ten_min_winds,
        six_hourly_winds,
    )


def drop_nans_DWD(data):
    data["day"] = pd.to_datetime(data["date"]).dt.date
    # exclude all days where at least one value is <0
    mask = data.groupby("day")["FF_10"].apply(lambda x: (x < 0).any())
    valid_dates = mask[~mask].index
    data = data[data["day"].isin(valid_dates)]
    data.reset_index(drop=True, inplace=True)

    # exclude all days where at least one value is missing
    count = data["day"].value_counts()
    data = data[data["day"].map(count) == (24 * 6)]
    data.reset_index(drop=True, inplace=True)
    return data


def set_date_DWD(data, date="MESS_DATUM"):
    data[date] = data[date].astype(str)
    day = (
        data[date].str[0:4]
        + "-"
        + data[date].str[4:6]
        + "-"
        + data[date].str[6:8]
        + " "
        + data[date].str[8:10]
        + ":"
        + +data[date].str[10:12]
        + ":00"
    )
    data["date"] = pd.to_datetime(day)
    data.set_index(["date"])
