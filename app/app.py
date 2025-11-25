"""
Entrypoint script that uses the scraper and repository modules.

This module orchestrates fetching data for multiple cities defined in a YAML
file and stores the results in Redis.
"""

import time
import yaml
from repository.redis_repository import WeatherRepository
from scraper.accuweather import get_temperature

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )
}

def load_cities():
    """Loads city data from cities.yml."""
    try:
        with open("cities.yml", "r") as f:
            return yaml.safe_load(f)["capitais"]
    except FileNotFoundError:
        print("Erro: O arquivo cities.yml não foi encontrado.")
        return []
    except (yaml.YAMLError, KeyError) as e:
        print(f"Erro ao ler ou processar o arquivo cities.yml: {e}")
        return []

def main() -> None:
    repo = WeatherRepository()
    cities = load_cities()

    if not cities:
        print("Nenhuma cidade para processar. Finalizando.")
        return

    print(f"Cidades a serem processadas: {[city['nome'] for city in cities]}")

    try:
        while True:
            print("-" * 20)
            for city in cities:
                city_name = city["nome"]
                city_url = city["url"]
                city_key = f"temperatura:{city_name}"
                
                print(f"Buscando temperatura para: {city_name}")
                temp = get_temperature(city_url, HEADERS)

                if temp:
                    print(f"Temperatura em {city_name}: {temp}°C")
                    try:
                        repo.save_temperature(city_key, temp)
                        print(f"Salvo em Redis: {city_key} -> {temp}")
                    except Exception as e:
                        print(f"Erro ao salvar no repositório para {city_name}: {e}")
                else:
                    print(f"Não foi possível obter a temperatura para {city_name}.")

            sleep_seconds = 100 * 60
            print("-" * 20)
            print(f"Aguardando {sleep_seconds} segundos até o próximo ciclo...")
            time.sleep(sleep_seconds)
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário, finalizando.")


if __name__ == "__main__":
    main()
