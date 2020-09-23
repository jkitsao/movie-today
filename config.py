import os 

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/movie/{}?api_key={}"
    MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simplemde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = "postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5"

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgres://osjdxommkpajya:331568f21e2091dbffde86f61ff2c8d8598cf8d44482174f7d4d2fcc29c5e143@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d4ji8t73b1mtp5"
    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}