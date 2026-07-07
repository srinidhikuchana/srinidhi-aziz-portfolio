#!/bin/bash
set -e
PROJECT_DIR="$HOME/srinidhi-aziz-portfolio"
VENV_DIR="python3-virtualenv"

echo "Step 1: Moving into project folder..."
cd "$PROJECT_DIR"

echo "Step 2: Pulling latest changes from main..."
git fetch && git reset origin/main --hard

echo "Step 3: Installing dependencies in virtual environment..."
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
deactivate

echo "Step 4: Restarting myportfolio service..."
systemctl restart myportfolio

echo "Redeploy complete. Site should be live."
