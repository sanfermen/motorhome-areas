import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import requests
import support_weather as sw

st.title("Motorhome Areas")

st.subheader("Map of Europe Areas")

st.caption("If you select one of the areas, you can see its index")

df= pd.read_csv("sobre-la-marcha/files/03-areas_country.csv", index_col = 0)


map = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=5, control_scale=True)

for index, location_info in df.iterrows():
    if location_info["price"] == "Free":
        folium.Marker([location_info["latitude"], location_info["longitude"]], tooltip=location_info["town"], popup=index, icon=folium.Icon(color='blue', prefix='fa',icon='van-shuttle')).add_to(map)
    elif location_info["price"] == "Paying":
        folium.Marker([location_info["latitude"], location_info["longitude"]], tooltip = location_info["town"], popup=index, icon=folium.Icon(color='red', prefix='fa',icon='van-shuttle')).add_to(map)

st_data = st_folium(map, width = 800)
st_data

area = st.number_input("Insert the area index")
df1 = sw.clima(df, area)

df_area = pd.DataFrame(df.loc[area,:]).T

st.subheader("Your selected area")
st.dataframe(df_area)

st.subheader("Next 7 days weather")
st.dataframe(df1)