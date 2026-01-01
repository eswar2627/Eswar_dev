from django.apps import AppConfig
import os
from django.contrib.auth import get_user_model

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        if os.getenv("CREATE_SUPERUSER") == "True":
            User = get_user_model()
            username = os.getenv("SU_NAME")
            password = os.getenv("SU_PASSWORD")
            email = os.getenv("SU_EMAIL", "")

            if username and password:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_superuser(
                        username=username,
                        email=email,
                        password=password
                    )
