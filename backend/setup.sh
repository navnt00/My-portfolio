#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create media directories
mkdir -p media/profile media/projects media/skills media/tech_icons

# Make migrations and migrate
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py add_sample_data

# Run server
python manage.py runserver 