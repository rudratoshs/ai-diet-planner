# src/config/settings.py
from .environment import env

DATABASE_URL = f"postgresql://{env.POSTGRES_USER}:{env.POSTGRES_PASSWORD}@{env.POSTGRES_HOST}:{env.POSTGRES_PORT}/{env.POSTGRES_DB}"

REDIS_URL = f"redis://{':' + env.REDIS_PASSWORD + '@' if env.REDIS_PASSWORD else ''}{env.REDIS_HOST}:{env.REDIS_PORT}/0"

# API Settings
API_V1_PREFIX = "/api/v1"
PROJECT_NAME = "RBAC Service"

# CORS Settings
ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Frontend local
    "http://localhost:8000",  # Backend local
]

# Cache Settings
CACHE_TTL = 3600  # 1 hour