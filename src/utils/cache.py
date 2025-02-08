# src/utils/cache.py
import redis
from functools import wraps
import json
from ..config.settings import REDIS_URL, CACHE_TTL

redis_client = redis.from_url(REDIS_URL)

def cache_decorator(ttl: int = CACHE_TTL):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Create cache key from function name and arguments
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # Try to get from cache
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return json.loads(cached_result)
            
            # Execute function and cache result
            result = await func(*args, **kwargs)
            redis_client.setex(
                cache_key,
                ttl,
                json.dumps(result, default=str)
            )
            return result
        return wrapper
    return decorator