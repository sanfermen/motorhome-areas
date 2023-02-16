import pandas as pd
import requests

def clima(dataf, indice):
    """
    Get the weather for next week of a specified location
        Parameters:
            Dataframe, index number of the area
        Return:
            A dataframe with the predictions
    """
    # hacemos la llamada  a la API
    url = f'https://api.open-meteo.com/v1/forecast?latitude={dataf.loc[indice,"latitude"]}&longitude={dataf.loc[indice,"longitude"]}&daily=weathercode&timezone=auto'

    dict_clima = {0: "Clear sky", 
                1: "Mainly clear", 
                2: "Partly cloudy", 
                3: "Overcast", 
                45: "Fog", 
                48: "Depositing rime fog", 
                51: "Light Drizzle", 
                53: "Moderate Drizzle", 
                55: "Dense intensity Drizzle", 
                56: "Light Freezing Drizzle", 
                57: "Dense intensity Freezing Drizzle",
                61: "Slight rain",
                63: "Moderate rain",
                65: "Heavy rain",
                66: "Light Freezing Rain",
                67: "Heavy Freezing Rain",
                71: "Slight Snow fall",
                73: "Moderate Snow fall",
                75: "Heavy Snow fall",
                77: "Snow grains",
                80: "Slight Rain showers",
                81: "Moderate Rain showers",
                82: "Violent Rain showers",
                85: "Slight Snow showers",
                86: "Heavy Snow showers",
                95: "Thunderstorm",
                96: "Thunderstorm with slight hai",
                99: "Thunderstorm with heavy hai"}
            
    response = requests.get(url=url)
    codigo_estado = response.status_code
    razon_estado = response.reason

    respuesta = response.json()
    dict = respuesta["daily"]
    dia = dict["time"]
    code = dict["weathercode"]
    for num, i in enumerate(code):
        for k,v in dict_clima.items():
            if i == k:
                code[num] = v
    df_3 = pd.DataFrame(code, index= dia, columns= ["Weather"]).T
    return df_3