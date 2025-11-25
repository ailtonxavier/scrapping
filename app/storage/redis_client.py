import os
import redis
from typing import Optional


def get_redis() -> redis.Redis:
    """Create and return a Redis client using environment variables.

    Defaults to localhost:6379 when not running in Docker compose.
    """
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", "6379"))
    return redis.Redis(host=host, port=port, decode_responses=True)


def ping_redis() -> bool:
    try:
        r = get_redis()
        return r.ping()
    except Exception:
        return False
