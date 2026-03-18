import requests
import os
from dotenv import load_dotenv 

load_dotenv()

def ver_idiomas():
   
    endpoint = os.getenv("ENDPOINT_TRANSLATOR")
    path = '/languages?api-version=3.0'
    constructed_url = endpoint + path

    headers = {
        'Content-type': 'application/json',

    }
    try:
        request = requests.get(constructed_url, headers=headers)
        response = request.json()

        idiomas = response["translation"] 

        idiomas_dict={}
        for codigo, info in idiomas.items():
            idiomas_dict[codigo] = info["name"]
        return idiomas_dict
    except Exception as e:
        print(f"Error al obtener idiomas: {e}")
        return {}

print(ver_idiomas())