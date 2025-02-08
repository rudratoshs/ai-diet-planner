# scripts/deploy.sh
#!/bin/bash
set -e

echo "Deploying RBAC Service..."

# Pull latest changes
git pull origin main

# Build docker image
docker-compose build

# Run migrations
docker-compose run --rm rbac-service alembic upgrade head

# Restart services
docker-compose up -d

echo "Deployment completed successfully!"