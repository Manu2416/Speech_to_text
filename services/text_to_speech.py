import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv 

load_dotenv()
def texto_voz():
    speech_config = speechsdk.SpeechConfig( #Configura la conexión con Azure
        subscription=os.getenv("SPEECH_KEY"),
        region= os.getenv("REGION")
    )

    # el idioma de la voz que queremos 
    speech_config.speech_synthesis_voice_name = 'es-MX-DaliaNeural'

    # Salida del audio
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # Crear el sintetizador 
    speech_synthesizer = speechsdk.SpeechSynthesizer( 
        speech_config=speech_config,
        audio_config=audio_config
    )

    # Texto a sintetizar
    text = input("Introduce el texto")

    #resultado 
    result = speech_synthesizer.speak_text_async(text).get()

 
    return(result)

texto_voz()
 