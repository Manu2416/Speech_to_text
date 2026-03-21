import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv 

load_dotenv()


def reconocimiento_de_voz():
    speech_config = speechsdk.SpeechConfig(#Configura la conexión con Azure
        subscription= os.getenv("SPEECH_KEY"),
        region=os.getenv("REGION")
    )
    #reconocer idioma
    speech_config.speech_recognition_language = "es-ES"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True) #Un objeto de configuración de audio.

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)#reconoce la voz

    print("Escuchando....")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()#escucha

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return "Recognized: {}".format(speech_recognition_result.text)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            return "Error details: {}".format(cancellation_details.error_details)
           