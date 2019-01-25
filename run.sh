#!/bin/bash
# Author: Herman Bonnes
set -e

# Create virtual environment
if [ ! -d "venv" ]; then
  python3 -m venv venv
  . venv/bin/activate
fi

# Install dependencies
# Yum
# Microsoft SQL Server ODBC
#sudo yum remove -y unixODBC-utf16 unixODBC-utf16-devel 
#sudo ACCEPT_EULA=Y yum install msodbcsql17
#sudo ACCEPT_EULA=Y yum install mssql-tools
#echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
#echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
#source ~/.bashrc
#sudo yum install -y unixODBC-devel
# Python
pip3 install -f ./dependencies/ --no-index -r ./dependencies/requirements.txt

# Run the application
export FLASK_APP=index.py
export FLASK_ENV=development # for Development purposes
flask run -p 80 --host=0.0.0.0
