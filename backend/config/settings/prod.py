from .base import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")  # noqa: F405
