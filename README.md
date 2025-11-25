<div align="center">🌡️ Weather Scraper & Redis Updater</div>
<div align="center"> <img src="https://media.tenor.com/xI7Y9zVYdFwAAAAM/pengu-pudgy.gif" width="200"> </div>

Sobre o projeto

Esse app pega a temperatura atual de várias cidades, usando scraping no AccuWeather, e salva tudo no Redis.
Ele segue SRP (Single Responsibility Principle) e usa Singleton nos lugares certos, tipo na conexão do Redis e no repositório.

A lógica fica separada em módulos bem leves:

Scraper → pega HTML, extrai temperatura

Repository → salva/consulta no Redis

City Loader → lê o arquivo cities.yml

Update Service → coordena o processo de atualização

Sleep Timer → controla o intervalo entre ciclos

Entrypoint (main.py) → só junta tudo e roda
