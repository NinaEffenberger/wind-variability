import geopandas
import matplotlib.pyplot as plt
from pyproj import CRS, Transformer
from tueplots import axes, cycler, figsizes, fonts, fontsizes
from tueplots.constants.color import palettes

colors = palettes.tue_plot
plt.rcParams.update({"figure.dpi": 150})
plt.rcParams.update({"hatch.color": colors[1]})
plt.rcParams["hatch.linewidth"] = 3
# plt.rcParams.update(fontsizes.icml2022())
# plt.rcParams.update(fonts.icml2022())
plt.rcParams.update(axes.lines())
plt.rcParams["text.usetex"] = True
file = geopandas.read_file("data/raw_data/renewables/windpower.shp")
lat, long = (file.X_coord, file.Y_coord)
# from coordinates are in ETRS 1989, to coordinates are epsg:4326
transformer = Transformer.from_crs(crs_from="epsg:3035", crs_to="epsg:4326")
x, y = transformer.transform(long.values, lat.values)

turbines = geopandas.GeoDataFrame(
    file,
    geometry=geopandas.points_from_xy(y, x),
)

print(file)
print(turbines)
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
germany = world[world.name == "Germany"]
fig, ax = plt.subplots(1, 1, figsize=(5, 6), constrained_layout=True)
ax.axis("off")
germany.plot(ax=ax, color=colors[2])
turbines.plot(ax=ax, color=colors[0], markersize=3, label="Turbine Locations")
plt.legend()
# plt.savefig("plots/turbine_locations_germany.pdf")

plt.show()
