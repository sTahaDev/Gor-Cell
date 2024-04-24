import source.libs.assistant
import source.libs.dedection
import sys
import source.libs.services
from datetime import datetime
import json
import requests
import time

class Program:
    def __init__(self) -> None:
        self.asistan = source.libs.assistant.Asistant()
        self.dedector = source.libs.dedection.Detector()
        self.weatherApi = source.libs.services.WeatherApi()
        self.settings = json.loads(self.__readFile("./settings.json"))
        self.newsApi = source.libs.services.NewsApi()
        pass
    def __readFile(self,url):
        with open(url,"r") as file:
            return file.read()
            
        pass
    def __asistanFuncsAdding(self):
        #asistana işlev ekle
        self.asistan.SystemFuncs.append({"qn": ["ne haber"], "func": lambda: (
            
            self.asistan.speak("iyi sen")
        )})

        self.asistan.SystemFuncs.append({"qn": ["kapat","görüşürüz"], "func": lambda: (
            self.asistan.speak("Görüşmek Üzere"),
            sys.exit()
        )})

        self.asistan.SystemFuncs.append({"qn": ["adım ne","ismim ne","benim adım ne"], "func": lambda: (
            self.asistan.speak("Senin adın " + self.settings["userName"] + ". Sen benim en yakın arkadaşımsın.")
        )})

        self.asistan.SystemFuncs.append({"qn": ["saat kaç","saat ne","saati söyle","saat ney"], "func": lambda: (
            self.asistan.speak("Saat " + str(datetime.now().hour) + "  " + str(datetime.now().minute))
        )})


        def isThereHuman():
            isHave,faceLength = self.dedector.detect_face()
            if(isHave):
                self.asistan.speak("Evet " + str(faceLength) + " tane var")
            else:
                self.asistan.speak("Hayır yok")
            pass
        self.asistan.SystemFuncs.append({"qn": ["insan var mı","100 var mı","biri var mı","biri mi var","kaç tane 100 var","kaç tane insan var"], "func": isThereHuman})

        def whatIsDate():
            gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
            today = datetime.now().date()
            todayIndex = today.weekday()
            self.asistan.speak("Bugün {}, {} .".format(gunler[todayIndex], today))
            
            pass
        self.asistan.SystemFuncs.append({"qn": ["bugün günlerden ne","günlerden ne","hangi gündeyiz","bugün ayın kaçı","ayın kaçı bugün","günlerden ne"], "func": whatIsDate})

        def whatIsWeather():
            translater = {
                "Thunderstorm": "Şiddetli Yağmurlu",
                "Drizzle": "Hafif Yağmurlu",
                "Rain": "Yağmurlu",
                "Snow": "Karlı",
                "Mist": "Dumanlı",
                "Smoke": "Dumanlı",
                "Haze": "Dumanlı",
                "Dust": "Tozlu",
                "Fog": "Sisli",
                "Sand": "Kumlu",
                "Ash": "Küllü",
                "Squall": "Şiddetli Fırtınalı",
                "Tornado": "Tornado",
                "Clear": "Açık",
                "Clouds": "Bulutlu"
            }

            weatherInfo = self.weatherApi.getWeather(self.settings["city"])

            weather = translater[weatherInfo["weather"][0]["main"]]
            temp = weatherInfo["main"]["temp"]
            city = weatherInfo["name"]
            
            self.asistan.speak(city.lower() +" için hava durumu: " + weather + " , " + str(int(temp)) + "derece." )

            pass
        self.asistan.SystemFuncs.append({"qn": ["hava nasıl","hava durumunu söyle","hava durumu ne","hava durumu"], "func": whatIsWeather})

        def readStory():
            self.asistan.speak("Hikaye okuma özelliği gelecek yakında")
            pass

        self.asistan.SystemFuncs.append({"qn":["hikaye oku"],"func":readStory})

        def readNews():
            self.asistan.speak("Görsell Haber Sunar: İşte bu günün en çok okunanları: ")

            newsIndex = 1
            for i in self.newsApi.getCuffs():
                self.asistan.speak(str(newsIndex) +".Haber: " + str(i) + " . ")
                newsIndex += 1
            
            self.asistan.speak("Görsell Haber sunar. Sağlıcakla kalın.")
            time.sleep(0.5)
            
            pass
        self.asistan.SystemFuncs.append({"qn":["haberler","gündemi oku","yeni haberler","haberleri oku","haber","gündem","gündem ne","haberler ne"],"func":readNews})

        def isThereLight():
            lightSize = self.dedector.detect_light()
            maxLight = 100
            midLight = 20
            if(lightSize >= maxLight):
                self.asistan.speak("Etraf Aydınlık")
                pass
            elif (lightSize <= maxLight and lightSize >= midLight):
                self.asistan.speak("Etraf Loş")
                pass
            elif (lightSize < midLight):
                self.asistan.speak("Etraf Karanlık")
                pass
            pass
        self.asistan.SystemFuncs.append({"qn":["ışık var mı","hava aydınlık mı","etraf aydınlık mı","hava aydınlık mı","ortam nasıl"],"func":isThereLight})
        pass

    
    def setup(self):
        #Assitanın koşullı işlemlerini ekleme
        self.__asistanFuncsAdding()
        pass

    def run(self):

        #asistanı run etmeyi unutma
        while True:
            self.asistan.run()
        pass