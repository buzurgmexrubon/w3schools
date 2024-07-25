from settings.base import *
from settings.app_settings.installed_apps import *
from settings.middlewares import *
from settings.templates import *
from settings.password_validation import *
from settings.internationalization import *
from settings.media import *

IS_DEVELOPMENT = os.getenv("IS_DEVELOPMENT", False)

if IS_DEVELOPMENT:
    try:
        from settings.environment_settings.development import *
    except ImportError:
        pass
else:
    try:
        from settings.environment_settings.production import *
    except ImportError:
        pass
