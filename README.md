# Wind Speed Variability

Code for the Paper "insert name"

All data subsets used are stored in `data`. To re-run the full experiments, download the raw data files as described below, add them to the folder `bigdata` and run the code in `pre-process`.

### Raw Data 
Wind speed data is from the [Kelmarsh wind farm](https://zenodo.org/record/5841834), the [Penmanshield wind farm](https://zenodo.org/record/5946808), the [Owez high tower](https://talltowers.bsc.es/node/4856) and the [NWTC M5 high tower](https://talltowers.bsc.es/node/4846) and from the [Deutsche Wetterdienst](https://opendata.dwd.de/climate_environment/CDC/).

CMIP6 data is from the model MPI-ESM1-2-LR and can be downloaded through the [ESGF node](https://esgf-node.llnl.gov/search/cmip6/).

### Install dependencies
```shell
cd path/to/wind-variability
pip install -r requirements.txt
```