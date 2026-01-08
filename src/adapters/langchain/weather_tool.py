import requests
from src.adapters.langchain.i_tool import ILangTool


class WeatherTool(ILangTool):
    def __init__(self):
        self.api_key = ""
        # self.api_key = "cb90bda3dc2a495db95202253250612"

        self.api_url = "https://api.weatherapi.com"

    def execute(self, city: str) -> str:
        return self.request_weather(city=city)

    def request_weather(self, city):

        query = f"{self.api_url}/v1/forecast.json?key={self.api_key}&q={city}&days=1&aqi=no&alerts=no"

        response = requests.get(url=query)
        try:
            response.raise_for_status()
            response_json = response.json()
            current_time = response_json["current"]
            current_temperature = current_time["temp_c"]
            condition = current_time["condition"]["text"]
        except Exception as e:
            print("Error a la hora de llamar")
            return {"resupuesta": "error en la llamada al servidor del tiempo"}
        return {"temperature_centigrados": current_temperature, "condicion": condition}


# @tool
# def obtener_tiempo(ciudad: str) -> str:
#     """
#     Función que devuelve el tiempo que hace en una ciudad determinada
#     Args:
#         ciudad: ciudad cuyo tiempo se quiere conocer
#     """
#     return request_weather(city=ciudad)


# def request_weather(city):

#     api_key = "cb90bda3dc2a495db95202253250612"
#     formatted_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"

#     response = requests.get(url=formatted_url)
#     try:
#         response.raise_for_status()
#         response_json = response.json()
#         current_time = response_json["current"]
#         current_temperature = current_time["temp_c"]
#         condition = current_time["condition"]["text"]
#     except Exception as e:
#         print("Error a la hora de llamar")
#     return {"temperature_centigrados": current_temperature, "condicion": condition}


if __name__ == "__main__":
    print(request_weather("london"))
