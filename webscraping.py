import requests
from bs4 import BeautifulSoup
import re

class ObjetoURL:
    def __init__(self, city, url):
        self.city = city
        self.url = url

listaUrl = [
    ObjetoURL("Sabara", "https://www.climatempo.com.br/previsao-do-tempo/cidade/186/sabara-mg"),
    ObjetoURL("Caete", "https://www.climatempo.com.br/previsao-do-tempo/cidade/116/caete-mg"),
    ObjetoURL("Ravena", "https://www.climatempo.com.br/previsao-do-tempo/cidade/5882/ravena-mg"),
    ObjetoURL("Taquaracu", "https://www.climatempo.com.br/previsao-do-tempo/cidade/4068/taquaracudeminas-mg"),
    ObjetoURL("Belohorizonte", "https://www.climatempo.com.br/previsao-do-tempo/cidade/107/belohorizonte-mg")    
]

for objeto in listaUrl:
    print(f"ID: {objeto.city}, Nome: {objeto.url}")

    response = requests.get(objeto.url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Get the temperature Min
    temperature_element = soup.select_one("#min-temp-1")
    temperature_min = temperature_element.text.strip()
    print("Temperatura Min:", temperature_min)

    # Get the temperature Max
    temperature_element_max = soup.select_one("#max-temp-1")
    temperature_max = temperature_element_max.text.strip()
    print("Temperatura Max:", temperature_max)

    # Get the Rain
    temperature_element_rain = soup.select_one("._margin-l-5")
    temperature_rain = temperature_element_rain.text.strip().replace('\n', '')
    print("Chuva:", temperature_rain)

    # Get the wind
    speed_element_wind = soup.select_one("#mainContent div:nth-of-type(5) div:nth-of-type(4) div:nth-of-type(1) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) ul li:nth-of-type(3) div")
    speed_wind = re.sub(r'<span class="arrow _margin-r-10" style="transform: rotate\(\d+deg\);"></span>', '', speed_element_wind.decode_contents()).replace('\n', '')
    print("Velocidade Vento:", speed_wind)
    
    # Get the moisture
    element_moisture = soup.select_one("#mainContent div:nth-of-type(5) div:nth-of-type(4) div:nth-of-type(1) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) ul li:nth-of-type(4) div p span:nth-of-type(1)")
    moisture = element_moisture.text.strip()
    print("Umidade:", moisture)

    # Get the Hour Sun
    element_sun = soup.select_one("#mainContent div:nth-of-type(5) div:nth-of-type(4) div:nth-of-type(1) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) ul li:nth-of-type(5) span:nth-of-type(2)")
    hour_sun = element_sun.text.strip().replace('\n', '')
    print("Horas de SOL:", hour_sun)