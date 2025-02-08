# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import roles, permissions, assignments, auth  # Add auth here
from .config.settings import API_V1_PREFIX, PROJECT_NAME, ALLOWED_ORIGINS
from .utils.logging import logger
from src.db.seeders.seed_roles import seed_roles,seed_permissions
from src.db.session import SessionLocal

app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_V1_PREFIX}/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=API_V1_PREFIX)  # Add this line
app.include_router(roles.router, prefix=API_V1_PREFIX)
app.include_router(permissions.router, prefix=API_V1_PREFIX)
app.include_router(assignments.router, prefix=API_V1_PREFIX)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting RBAC service")
    db = SessionLocal()
    try:
        seed_permissions(db)
        seed_roles(db)
    finally:
        db.close()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down RBAC service")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}