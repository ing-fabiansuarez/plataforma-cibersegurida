from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()

class Command(BaseCommand):
    help = 'Create superuser if it does not exist'

    def handle(self, *args, **options):
        username = 'fsuarez120'
        email = 'fsuarez120@unab.edu.co'
        password = 'Qwerty123456*'

        try:
            with transaction.atomic():
                # Check if user already exists
                if User.objects.filter(username=username).exists():
                    self.stdout.write(
                        self.style.WARNING(f'Superuser "{username}" already exists.')
                    )
                    return

                # Create superuser
                user = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                    role='ADMIN'
                )
                
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully created superuser "{username}" with email "{email}"'
                    )
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
            raise
