# Habits
This project aims to study habits and routine on an individual basis. It has been developed in the context of the course \Studies on Human Behaviour\, offered by the University of trento, during the academic year 2021/22.

## Project Goal
The goal of the project is to examine activities and habits, taking into account the four main triggers influencing the development of a habit, namely time, location, mood, and people. 

## Data
Data were collected for two weeks, from 13 October 2021 to 27 October 2021, in the context of the [WeNet](https://www.internetofus.eu/) project.
To collect these data, each partecipant used the iLog app, installed on their mobile devices.
The data collected are both coming from mobile sensors and self-reported data, as the app would send questions to the partecipant every half an hour.
This project uses data collected by a single person, namely myself.

## Project Structure
- `TimeDiaries_preprocessing.ipynb`, `Bluetooth_preprocessing.ipynb`, `Location_preprocessing.ipynb`: these notebooks were used to clean and pre-process data coming from timediaries, bluetooth, and GPS respectively.
- `match_location_mood_bluetooth.ipynb`: this notebook was used to merge together the three files coming from the notebooks above, taking into account the different intervals of data collections, thus following specific criteria to merge them.
- `chart-act-day.ipynb`: this notebook was used to produce a chart of activities divided by day of the week and to observe changes in behaviour between working days and weekends.
- `activity-during-day.R`: plot to visualize how the different activities distribute during the hours of the day.
- `maps_data_preparation-ipynb`: used to prepare data for the creation of the following maps.
- `map_all_locations.ipynb`: projects on a map all the GPS locations collected during the two weeks of data collections, and groups them in clusters; when available, the markers also report data coming from timediaries.
- `bluetooth_map-ipynb`: produces a map focused on social interactions by location. Markers are colored differently according to the number of people around in that specific place, on average (zero, between 1 and 3, 4 or more).
- `mood_map_folium.ipynb`: the focus of this map is to represent activities by locations: for each location, it reports the top 3 most frequent activities the user reported to have done there. It also allows to have an idea of the points of interest, as markers are colored by frequence of attendance of the place.
- `BBN_data_preprocessing.ipynb`: notebook used to pre-process data before feeding them into the Bayesian Network: data concerning activities were grouped into homogeneous categories, missing values were covered, places were recoded, and a new variable for time (morning/afternoon/evening) was created.
- `BBN-complete.ipynb`: notebook defining the structure of the Bayesian Network and outputing the probabilities.
- `BN_interface.py`: a simple interface produced using tkinter, which allows to interact with the Bayesian Network and get conditional probabilities concerning the activity that would be performed, provided some evidence for the other variables (time of the day, emotional state, location, and number of people).

## Important note:
The result of the Bayesian Network in terms of probabilities are NOT meant to be generalized, rather they are specific to the user to which the data refers to, and most likely, also to the well-defined timeframe considered. Different users may have very different results. 

## Installing dependencies
In order to install all the needed packages, use the following command:
```bash
pip install -r requirments.txt
```
