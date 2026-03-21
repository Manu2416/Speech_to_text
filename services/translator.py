# services/translator.py
import requests
import os
from dotenv import load_dotenv 


load_dotenv()

def traducir_texto(texto, idioma_origen, idioma_destino):
    # Traemos las llaves del .env
    endpoint = os.getenv("ENDPOINT_TRANSLATOR")
    manukey = os.getenv("TEXT_KEY")
    region = os.getenv("REGION")
    
    path = '/translate'
    url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': idioma_origen,
        'to': [idioma_destino] 
    }

    headers = {
        'Ocp-Apim-Subscription-Key': manukey,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
    }
    
    body = [{'text': texto}]

    try:
        request = requests.post(url, params=params, headers=headers, json=body)
        request.raise_for_status() 
        response = request.json()
        return response[0]["translations"][0]["text"]
    except Exception as e:
        return f"Error en la traducción: {str(e)}"
