import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # car problème réseau
                                                                    # entreprise


# ici l'API renvoit directement la température en Celsius, donc pas besoin de conversion
def KelvinToCelsius(Tkelvin):
    """Convert temperature from Kelvin to Celsius
       arrondi."""
    Tcelsius = Tkelvin - 273.15
    return Tcelsius


def MessageVilleEtTemperature(ville, temperature):
    """Return a message with the city and its temperature in Celsius."""
    print(f"La température à {ville} est de {temperature}°C.")


def GetTemperatureFromAPI(ville, api_key):
    """Get the temperature in Kelvin from the OpenWeatherMap API."""
    
    # Construire l'URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"

    # Faire la requête
    response = requests.get(url, verify=False)  # car problème réseau entreprise

    # Vérifier que la requête a réussi (code HTTP 200)
    if response.status_code != 200:
        raise Exception(f"Erreur lors de la requête à l'API: {response.status_code}")

    # réponse au format JSON
    data = response.json()

    temperature = data["main"]["temp"]

    return temperature


def FonctionExercice7(temperatures_list):
    
    i = 0

    for temperature in temperatures_list:
        if temperature > 20:
            i += 1
    
    return i


if __name__ == "__main__":
    
    # # Exercice 5
    # Tkelvin = 40+273.15
    # Tcelsius = KelvinToCelsius(Tkelvin)  
    # MessageVilleEtTemperature("Paris", Tcelsius)

    # # Exercice 6
    # api_key = "62b32cf2876cbabbd135b211f0b4c4f3"
    # ville = "Paris"
    # temperature = GetTemperatureFromAPI(ville, api_key)
    # MessageVilleEtTemperature(ville, temperature)

    # Exercice 7
    ListeTemp = [20, 18, 22, 25, 19, 21, 17, 23, 20]
    NombreJoursDansListe = len(ListeTemp)
    compteur = FonctionExercice7(ListeTemp)
    print(f"Il y a dans cette liste {compteur} jour(s) sur {NombreJoursDansListe} avec "
           "une température supérieure à 20°C")
