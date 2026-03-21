import requests
import os
from dotenv import load_dotenv 

load_dotenv()
# Funcion de azure de detectar idioma
def detect(text):
    path = '/detect'
    endpoint = os.getenv("ENDPOINT_TRANSLATOR")
    region = os.getenv("REGION")
    manukey = os.getenv("TEXT_KEY")

    url =  endpoint + path

    # Build the request
    params = {
        'api-version': '3.0'
    }

    headers = {
    'Ocp-Apim-Subscription-Key': manukey,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json'
    }

    body = [{
        'text': text
    }]

    # Send the request and get response
    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()

    # Parse JSON array and get language
    
    language = response[0]["language"]
    return  language

