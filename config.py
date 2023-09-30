import os

class BaseConfig(object):
    # Define the database URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://bryan:PASS@localhost/game_store'
    
    def JWT_SECRET_KEY(self):
        secret_key = os.environ.get("JWT_SECRET")
        if secret_key is None:
            raise ValueError("Missing env JWT_SECRET")
        return secret_key

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    TESTING = True

# Create the app_config based on the FLASK_ENV environment variable
env = os.environ.get("FLASK_ENV")
if env == "development":
    app_config = DevelopmentConfig()
elif env == "production":
    app_config = ProductionConfig()
elif env == "testing":
    app_config = TestConfig()
else:
    raise ValueError("Invalid FLASK_ENV value")
