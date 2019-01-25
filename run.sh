#!/bin/bash
# Author: Herman Bonnes

# Create virtual environment
if [ ! -d "venv" ]; then
  python3 -m venv venv
  . venv/bin/activate
fi

# Install dependencies
pip install -f ./dependencies/ --no-index -r ./dependencies/requirements.txt

# Run the application
export FLASK_APP=index.py
# For development
export FLASK_ENV=development
flask run --host=0.0.0.0
