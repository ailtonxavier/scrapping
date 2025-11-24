import requests
from bs4 import BeautifulSoup

# A URL específica que você pediu
url = "https://www.accuweather.com/pt/br/natal/35658/weather-forecast/35658?city=natal"

# Headers continuam obrigatórios para fingir ser um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    print(f"Acessando: {url}...")
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Lógica de extração
        # DICA: No AccuWeather, a classe da temperatura geralmente é 'temp' ou 'display-temp'
        # Se retornar "N/A", clique com botão direito no site > Inspecionar para ver a classe atual
        elemento_temp = soup.find('div', class_='temp')
        
        temp = elemento_temp.text.strip() if elemento_temp else "N/A - Verifique a classe CSS"
        
        print(f"Clima em Natal: {temp}")
    else:
        print(f"Erro ao acessar a página. Status Code: {response.status_code}")

except Exception as e:
    print(f"Erro na execução: {e}")
