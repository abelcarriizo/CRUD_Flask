#!/bin/bash

# Check if packages are installed
command -v python3 >/dev/null 2>&1 || { echo >&2 "python3 is not installed. Aborting."; exit 1; }
dpkg-query -l python3-venv > /dev/null 2>&1 || { echo >&2 "python3-venv is not installed. Aborting."; exit 1; }
command -v pip >/dev/null 2>&1 || { echo >&2 "pip is not installed. Aborting."; exit 1; }

# Upgrade pip
python3 -m pip install --upgrade pip

# Preparation of the virtual environment
python3 -m venv .venv
. .venv/bin/activate

# Check the existence of the .env file
file=".env"
if [ ! -f "$file" ]; then
    echo "Generating .env..."
    # Prompts the user to enter the values of environment variables
    read -p "Ingrese el valor para USER: " user
    read -p "Ingrese el valor para PASSWORD: " password
    read -p "Ingrese el valor para HOST: " host
    read -p "Ingrese el valor para DATABASE: " database

    # Write the environment variables to the .env file
    echo "USER=$user" >> .env
    echo "PASSWORD=$password" >> .env
    echo "HOST=$host" >> .env
    echo "DATABASE=$database" >> .env

    echo ".env file created successfully."
fi

# Installation of dependencies
pip install -r requirements.txt
