from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="iJ8CbGPKKTtOMOFKW1S9xPuWeUJ1rrI73_9Yi4DTM_FhJrTrDuo", # type: ignore
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
