#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Replace these with your preferred credentials
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'password123')

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superuser '{USERNAME}' created successfully.")
else:
    print(f"Superuser '{USERNAME}' already exists.")
