# scripts/start.sh
#!/bin/bash
set -e

# Run database migrations
alembic upgrade head

# Start the application
uvicorn src.main:app --host 0.0.0.0 --port $SERVICE_PORT --reload