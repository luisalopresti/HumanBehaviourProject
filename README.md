# Human Behaviour: studies on habits
[name](link)

## Project Goal



## Project Structure
- `TimeDiaries_preprocessing.ipynb`, `Bluetooth_preprocessing.ipynb`, `Location_preprocessing.ipynb`: these notebooks were used to clean and pre-process data coming from timediaries, bluetooth, and GPS respectively.
- `match_location_mood_bluetooth.ipynb`: this notebook was used to merge together the three files coming from the notebooks above, taking into account the different intervals of data collections, thus following specific criteria to merge them.
- `chart-act-day.ipynb`: this notebook was used to produce a chart of activities divided by day of the week and to observe changes in behaviour between working days and weekends.
- `activity-during-day.R`: plot to visualize how the different activities distributes during the hours of the day.
- `maps_data_preparation-ipynb`: used to prepare data for the creation of the following maps.
- `map_all_locations.ipynb`: projects on a map all the GPS locations collected during the two weeks of data collections, and groups them in clusters; when available, the markers also report data coming from timediaries.
- `bluetooth_map-ipynb`: prodices a map focused on social interactions by location. Markers are colored differently according to the number of people around in that specific location, on average (zero, between 1 and 3, 4 or more).
- `mood_map_folium.ipynb`: the focus of this map is to represent activities by locations: for each location, it reports the top 3 most frequent activities the user reported to have done there. It also allows to have an idea of the points of interest, as markers are colored by frequence of attendance of the place.
- `BBN_data_preprocessing.ipynb`: notebook used to pre-process data before feeding them into the Bayesian Network: data were grouped into homogeneous categories, missing values were covered, and so on.
- `BBN-complete.ipynb`: notebook defining the structure of the Bayesian Network and outputing the probabilities.
- `BN_interface.py`: a simple interface produced using Tkinter, which allow to interact with the Bayesian Network and get conditional probabilities concerning the activity that would be performed, provided some evidence for the other variables (time of the day, emotional state, location, and number of people).

## Important note:
The result of the Bayesian Network in terms of probabilities are NOT meant to be generalized, rather they are specific for the user to which the data refers to, and most likely, also to the specific timeframe considered. Different users may have very different results. 

## Installing dependencies
In order to install all the needed packages, use the following command:
```bash
pip install -r requirments.txt
```
