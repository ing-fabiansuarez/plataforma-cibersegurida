#!/usr/bin/env python
"""
Script to create superuser during deployment
This script will be executed during the build process in Render
"""

import os
import sys
import django

# Add the project directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

def create_superuser():
    """Create superuser if it doesn't exist"""
    username = 'fsuarez120'
    email = 'fsuarez120@unab.edu.co'
    password = 'Qwerty123456*'

    try:
        with transaction.atomic():
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                print(f'Superuser "{username}" already exists.')
                return True

            # Create superuser
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role='ADMIN'
            )
            
            print(f'Successfully created superuser "{username}" with email "{email}"')
            return True
            
    except Exception as e:
        print(f'Error creating superuser: {str(e)}')
        return False

if __name__ == '__main__':
    print("Starting superuser creation process...")
    success = create_superuser()
    if success:
        print("Superuser creation process completed successfully!")
        sys.exit(0)
    else:
        print("Superuser creation process failed!")
        sys.exit(1)
