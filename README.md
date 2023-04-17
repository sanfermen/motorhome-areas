# MOTORHOME AREAS

![IMG20221226142923](https://user-images.githubusercontent.com/114421338/232432777-9283987d-79db-4b45-a996-c483fd333717.jpg)

The goal of this repo is to create a database and a streamlit app from a messy csv file.


## Repository Structure
- **Files**: All the files we are working with
- **Notebooks**:
  - *01-camper_areas.ipynb*: Extract the information from the original file
  - *02-camper_country.ipynb*: Get locations from ***Nominatim API***
  - *03-map_weather.ipyn*: Create a map with **folium** and get weather forecast from ***open-meto API***
  - *04-weather.ipynb*: With **meteostat**, create a dataframe with historical monthly temperature for each area
  - *app.py*: ***Streamlit app***. Write in the terminal `streamlit run app.py`
  - *foursquare.ipynb*: Obtain point of interest (supermarket, museum...) from ***Foursquare API*** :construction: **Work in Progress**
- **SQL_database**: Create a mySQL database with the information about the areas and the historical temperature

## Motorhome areas map
<img width="643" alt="map" src="https://user-images.githubusercontent.com/114421338/232441882-f927ea71-0248-44d5-869d-172c7db86349.png">

## Libraries
- Pandas
- Re
- Requests
- Folium
- Meteostat
- Datetime
- Numpy
- Streamlit
- Streamlit_folium
- Os
- Dotenv
- Time
- Mysql.connector
  


