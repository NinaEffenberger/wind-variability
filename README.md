# Wind Speed Variability

Code for the Paper "[Mind the (spectral) gap: How the temporal resolution of wind data affects multi-decadal wind power forecasts](https://iopscience.iop.org/article/10.1088/1748-9326/ad0bd6)" - Nina Effenberger, Rachel H. White, Nicole Ludwig.

All data subsets used are stored in `data`. To re-run the full experiments, download the raw data files as described below, add them to the folder `bigdata` and run the code in `pre-process`.

### Raw Data 
Wind speed data is from turbine 1 of the [Kelmarsh wind farm](https://zenodo.org/record/5841834), turbine 11 of the [Penmanshield wind farm](https://zenodo.org/record/5946808), the [Owez high tower](https://talltowers.bsc.es/node/4856) and the [NWTC M5 high tower](https://talltowers.bsc.es/node/4846) and from the [Deutsche Wetterdienst](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/wind/historical/), stations 00003 (Aachen), 05792 (Zugspitze), 00596 (Boltenhagen), 01357 (Fichtelberg).

CMIP6 data is from the model MPI-ESM1-2-LR and can be downloaded through the [ESGF node](https://esgf-node.llnl.gov/search/cmip6/). 10m wind speeds can be computed using the two wind direction variables vas and uas. Instantaneous wind speed frequency is 3hrPt and 6hrPt, average wind speed frequency is 3hr, 6hr and day. The variant label was chosen to be `r1i1p1f1`. 

### Install dependencies
```shell
cd path/to/wind-variability
pip install -r requirements.txt
```
