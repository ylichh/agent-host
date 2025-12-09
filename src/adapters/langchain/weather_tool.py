from langchain.tools import tool
import requests


@tool
def obtener_tiempo(ciudad: str) -> str:
    """
    Función que devuelve el tiempo que hace en una ciudad determinada
    Args:
        ciudad: ciudad cuyo tiempo se quiere conocer
    """
    return request_weather(city=ciudad)


def request_weather(city):

    api_key = "cb90bda3dc2a495db95202253250612"
    formatted_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no"

    response = requests.get(url=formatted_url)
    try:
        response.raise_for_status()
        response_json = response.json()
        current_time = response_json["current"]
        current_temperature = current_time["temp_c"]
        condition = current_time["condition"]["text"]
    except Exception as e:
        print("Error a la hora de llamar")
    return {"temperature_centigrados": current_temperature, "condicion": condition}


if __name__ == "__main__":
    print(request_weather("london"))
