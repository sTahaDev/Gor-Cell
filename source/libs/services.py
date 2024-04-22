import requests

class ApiRequest:
    def __init__(self) -> None:
        self.url = ""
        self.key = ""
        pass
    def get(self):
        response = requests.get(self.url)
        return response.json()
        pass
    

class weatherApi(ApiRequest):
    def __init__(self) -> None:
        super().__init__()

        self.cityName = ""
        self.key = "a22897bbcb27ac5f92c68010d28d2b67"
        self.__updateUrl()

        pass
    def __updateUrl(self):

        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.cityName}&appid={self.key}&units=metric"

    def getWeather(self,cityNamee):

        self.cityName = cityNamee
        self.__updateUrl()
        return self.get()
        