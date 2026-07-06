#!/bin/bash
set -e

PROJECT_DIR="$HOME/srinidhi-aziz-portfolio"
VENV_DIR="python3-virtualenv"
TMUX_SESSION="flask-session"

echo "Step 1: Killing all existing tmux sessions..."
tmux kill-server 2>/dev/null || echo "No tmux sessions running."

echo "Step 2: Moving into project folder..."
cd "$PROJECT_DIR"

echo "Step 3: Pulling latest changes from main..."
git fetch && git reset origin/main --hard

echo "Step 4: Installing dependencies in virtual environment..."
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
deactivate

echo "Step 5: Starting new detached tmux session with Flask server..."
tmux new-session -d -s "$TMUX_SESSION" "cd $PROJECT_DIR && source $VENV_DIR/bin/activate && export FLASK_APP=app && flask run --host=0.0.0.0 --port=5000"

echo "Redeploy complete. Site should be live."
