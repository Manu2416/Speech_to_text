import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv 
load_dotenv()
def texto_voz(text):
    try:
        speech_config = speechsdk.SpeechConfig(
            subscription=os.getenv("SPEECH_KEY"),
            region=os.getenv("REGION")
        )
        speech_config.speech_synthesis_voice_name = 'es-MX-DaliaNeural'

        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config
        )

        result = synthesizer.speak_text_async(text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Audio reproducido correctamente ✅")
        else:
            print("Error al reproducir audio:", result.reason)
        return result

    except Exception as e:
        print("Error en la síntesis de voz:", str(e))
        return None
