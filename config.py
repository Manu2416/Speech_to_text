import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SPEECH_KEY = os.getenv("SPEECH_KEY")
    SPEECH_REGION = os.getenv("SPEECH_REGION")#hola