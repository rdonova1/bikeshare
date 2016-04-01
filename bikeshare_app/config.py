"""Module containing configurations for the flask server"""
from os import getenv
# TODO: Setup a logging environment

# pylint: disable=too-few-public-methods
class BaseConfig(object):
    """The base configuration that should be used in production"""
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {'db': 'bikeshare'}

class TestingConfig(BaseConfig):
    """Configuration for running unit tests"""
    DEBUG = False
    TESTING = True
    MONGODB_SETTINGS = {'db': 'bikeshare-test'}

class DevelopmentConfig(BaseConfig):
    """The configuration that should be run during development"""
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {'db': 'bikeshare-test'}

CONFIG = {
    "development": "bikeshare_app.config.DevelopmentConfig",
    "testing": "bikeshare_app.config.TestingConfig",
    "default": "bikeshare_app.config.BaseConfig"
}

def configure_app(app):
    """Configure the app based on where it is deployed. First check for the
    FLASK_ENVIRONMENT environment variable, fallback to the default
    BaseConfig"""
    config_name = getenv("FLASK_ENVIRONMENT", "default")
    print(config_name)
    app.config.from_object(CONFIG[config_name])