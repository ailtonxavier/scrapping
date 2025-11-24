import requests
from bs4 import BeautifulSoup

url = "https://www.accuweather.com/pt/br/natal/35658/weather-forecast/35658?city=natal"

# Headers para fingir ser um navegador (Crucial para não ser bloqueado)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Estratégia 1: Tentar encontrar o card de "Tempo Atual" (Mais preciso)
        # A classe 'cur-con-weather-card__panel' geralmente contém o bloco de tempo atual
        current_weather_card = soup.find("div", class_="cur-con-weather-card__panel")
        
        if current_weather_card:
            # Dentro do card, procuramos a classe da temperatura
            temp_element = current_weather_card.find("div", class_="temp")
            if temp_element:
                print(f"Temperatura Atual: {temp_element.text.strip()}")
            else:
                print("Encontrei o card, mas não achei o número da temperatura.")
        
        # Estratégia 2 (Fallback): Pegar o primeiro elemento com classe 'temp' da página
        # Às vezes o layout muda e o primeiro .temp costuma ser o destaque
        else:
            print("Card específico não encontrado, tentando busca genérica...")
            generic_temp = soup.find("div", class_="temp")
            if generic_temp:
                print(f"Temperatura encontrada (pode ser previsão): {generic_temp.text.strip()}")
            else:
                print("Não foi possível encontrar a temperatura.")

    else:
        print(f"Erro na requisição: {response.status_code}")

except Exception as e:
    print(f"Erro no script: {e}")