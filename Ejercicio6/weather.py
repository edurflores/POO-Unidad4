import requests
import json

class Tiempo(object):

    def obtener(self, capital):
        aux = json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid=74f1de4f180cc980c8bb3ce8d3cbec7f".format(
                capital)).content)
        if "main" in aux:
            d = {
                "Temperatura": aux["main"]["temp"],
                "sensacion": aux["main"]["feels_like"],
                "humedad": aux["main"]["humidity"]
            }
        else:
            d = aux
        return d