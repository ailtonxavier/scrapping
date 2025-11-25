"""Repository package entrypoint.

Expose repository implementations from this module so callers can import
`from repository import WeatherRepository` (keeps older import paths working).
"""

from .redis_repository import WeatherRepository

__all__ = ["WeatherRepository"]
