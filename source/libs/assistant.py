
import time
import webbrowser
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os

    
class Asistant:
    def __init__(self) -> None:
        self.yourVoice = ""
        self.SystemFuncs = []
        self.voiceFile = "./source/assistantvoices"

        self.speak("Başlatılıyor...")

        pass

    def run(self):
        self.speak("Buyrun Dinliyorum")
        response = self.__record()
        self.yourVoice = response
        print(response)
        self.__execute(response)
            
        pass

    def __execute(self,response):
        for item in self.SystemFuncs:
            for i in item["qn"]:
                if response.lower() == i.lower():
                    item["func"]()
                    break
            
            
        pass

    #Sesi Algılama Ayarları
    def __record(self,ask = False):
        r = sr.Recognizer()
        if ask:
            self.speak(ask)
        with sr.Microphone() as source:
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language="tr-TR")
            except sr.UnknownValueError:
                self.speak("Anlayamadım")
            except sr.RequestError:
                self.speak("Üzgünüm! Sistem Çalışmıyor :(")

            return voice
        
    #Konuşturma
    def speak(self,string):
        tts = gTTS(string,lang="tr")
        rand = random.randint(1,10000)
        
        file = self.voiceFile+"/audio-"+str(rand)+".mp3"
        tts.save(file)
        playsound(file)
        os.remove(file)

    pass

    




