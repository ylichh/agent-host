from langchain.tools import tool


def crear_obtener_tiempo(tool_instance):
    @tool
    def obtener_tiempo(ciudad):
        """
        Función que devuelve el tiempo que hace en una ciudad determinada
        Args:
            ciudad: ciudad cuyo tiempo se quiere conocer
        """
        weather_tool = tool_instance
        return weather_tool.execute(city=ciudad)

    return obtener_tiempo


def crear_obtener_clima(tool_instance):
    @tool
    def obtener_clima(ciudad):
        """
        Función que devuelve una pequeña descripción sobre el clima que hay en distintas ciudades a lo largo
        del año.
        Args:
            ciudad: ciudad de cuyo clima se solicita una descripción
        """
        climate_tool = tool_instance
        return climate_tool.execute(ciudad)

    return obtener_clima
