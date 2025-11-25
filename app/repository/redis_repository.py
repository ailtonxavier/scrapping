from typing import Optional
from storage.redis_client import get_redis


class WeatherRepository:
    """Repository abstraction for storing/retrieving weather values in Redis."""

    def __init__(self):
        self._redis = get_redis()

    def save_temperature(self, city_key: str, temp_value: str) -> None:
        """Save a temperature value under a city key with a short TTL (optional)."""
        # store as plain string; clients can decide on TTL/structure
        self._redis.set(city_key, temp_value)

    def get_temperature(self, city_key: str) -> Optional[str]:
        return self._redis.get(city_key)
