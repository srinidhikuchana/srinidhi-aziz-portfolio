#!/bin/bash
set -e

PROJECT_DIR="$HOME/srinidhi-aziz-portfolio"

echo "Step 1: Moving into project folder..."
cd "$PROJECT_DIR"

echo "Step 2: Pulling latest changes from main..."
git fetch origin
git reset --hard origin/main

echo "Step 3: Building the latest production Docker image..."
docker compose -f docker-compose.prod.yml build

echo "Step 4: Restarting the myportfolio systemd service..."
systemctl restart myportfolio

echo "Step 5: Verifying that the service is active..."
systemctl is-active --quiet myportfolio

echo "Redeploy complete. The portfolio service is active."
