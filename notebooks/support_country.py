# Libraries

import requests
import pandas


def location(lat, lon):
    """
    Get the location of the motorhome area
        Parameters: 
            lat: latitude
            lon: longitude
        Returns:
            Town, City or municipality
    """
    # API request
    url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}'

    response = requests.get(url=url)
   
    respuesta = response.json()
    direccion = respuesta["address"]
    lista = direccion.keys()
    
    # Depending on country: town, city, village, municipality
    if "town" in lista:        
        return direccion["town"]
    elif "city" in lista:
        return direccion["city"]
    elif "village" in lista:
        return direccion["village"]
    elif "municipality" in lista:
        return direccion["municipality"]
    else:
        return "unknown"


def region(lat, lon):
    """
    Get the region of the motorhome area
        Parameters: 
            lat: latitude
            lon: longitude
        Returns:
            State, County or Country
    """
    # API requests
    url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}'

    response = requests.get(url=url)
       
    respuesta = response.json()
    direccion = respuesta["address"]
    lista = direccion.keys()
    
    if "state" in lista:
        return direccion["state"]
    elif "county" in lista:
        return direccion["county"]
    else:
        return direccion["country"]


def country(lat, lon):
    
    """
    Get the region of the motorhome area
        Parameters: 
            lat: latitude
            lon: longitude
        Returns:
            Country
    """
    # API requests
    url = f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={lat}&lon={lon}'

    response = requests.get(url=url)
   
    respuesta = response.json()
    direccion = respuesta["address"]
    lista = direccion.keys()
    
    return direccion["country"]