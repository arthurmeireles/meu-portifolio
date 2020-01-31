from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'
    STATIC_URL = '/static/'
    MEDIA_ROOT = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, "public")

