import re
import requests
import traceback
from datetime import datetime 
from bs4 import BeautifulSoup
from dbClimaTempo  import MySQLDados 
import horasCalculadora

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
    try:
        print(f"ID: {objeto.city}, Nome: {objeto.url}")

        response = requests.get(objeto.url)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        results = soup.find_all('div', attrs={'class': 'col-md-6 col-sm-12'})
        for div in results:
            filtros = div.find_all('ul')
            for filtro in filtros:
                result = filtro.find_all('span')
                for indice,li in enumerate(result):
                    if indice == 1:
                        temperature_min = li.text
                    if indice == 2:
                        temperature_max = li.text
                    if indice == 4:
                        rain = str(li.text).strip().replace('\n', '')
                    if indice == 8:
                        moisture_min = str(li.text).strip()
                    if indice == 9:
                        moisture_max = str(li.text).strip()
                    if indice == 11:
                        hour_sun = str(li.text).strip().replace('\n', '')

                result_vento = filtro.find_all('div')
                for indice,div_li in enumerate(result_vento):
                    if indice == 2:
                        speed_wind =str(div_li.text).replace('\n', '')
        moisture = moisture_min + moisture_max
        MySQLDados(datetime.now(), objeto.city,int(''.join(filter(str.isdigit, temperature_min))),int(''.join(filter(str.isdigit, temperature_max))),rain,speed_wind,moisture,horasCalculadora.CalcularHoras(hour_sun)).InsertDadaBase()
    except Exception as err:
        traceback.print_exc(err)