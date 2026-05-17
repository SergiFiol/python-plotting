import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explora la estructura de los datos
filename = "30_day_data_eq.json"
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]

#Mapea los terremotos

data = [{"type": "scattergeo",
		"lon": lons,
		"lat": lats,
		"marker": {"size": [3*mag for mag in mags],
		"color": mags,
		"colorscale": "earth",
		"reversescale": True,
		"colorbar": {"title": "Magnitude"}
			}
		}]


my_layout = Layout(title="Global Earthquakes Over One Month")

fig = {"data":data, "layout":my_layout}
offline.plot(fig, filename="global_eathquakes.html")
