#!/bin/bash
set -e

PROJECT_DIR="$HOME/srinidhi-aziz-portfolio"

echo "Step 1: Moving into project folder..."
cd "$PROJECT_DIR"

echo "Step 2: Pulling latest changes from main..."
git fetch
git reset origin/main --hard

echo "Step 3: Stopping current Docker containers..."
docker compose -f docker-compose.prod.yml down

echo "Step 4: Rebuilding and starting Docker containers..."
docker compose -f docker-compose.prod.yml up -d --build

echo "Redeploy complete. Site should be live."
