def KelvinToCelsius(Tkelvin):
    """Convert temperature from Kelvin to Celsius
       arrondi."""
    Tcelsius = Tkelvin - 273.15
    return Tcelsius


def MessageVilleEtTemperature(ville, temperature):
    """Return a message with the city and its temperature in Celsius."""
    print(f"La température à {ville} est de {temperature}°C.")


if __name__ == "__main__":
    
    Tkelvin = 40+273.15
    
    Tcelsius = KelvinToCelsius(Tkelvin)
    
    MessageVilleEtTemperature("Paris", Tcelsius)
