from .distributions import (compute_instantenous_windspeeds, gamma_paramsdef,
                            gamma_paramsdef_instanteous, weibull_paramsdef,
                            weibull_paramsdef_instanteous)
from .kolmogorov_smirnov import kolmogorov_smirnov_multi
from .windspeed_averages_wp import (compute_average_windspeeds,
                                    compute_windpower_generation,
                                    compute_windpower_generation_cmip,
                                    compute_windpower_generation_instantaneous,
                                    drop_nans, drop_nans_DWD, load_data,
                                    set_date, set_date_DWD)
