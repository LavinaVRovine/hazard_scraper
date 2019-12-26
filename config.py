import logging
import os

DATABASE_URI = "postgres://postgres:Darthpic0@localhost/"
# bookie names should reflect monitor class names
IMPLEMENTED_BOOKIES = {
    "LoL": {"IfortunaCz": "https://www.ifortuna.cz/cz/sazeni/progaming"},
    "Dota": {"IfortunaCz": "https://www.ifortuna.cz/cz/sazeni/progaming"},
    "CS:GO": {"IfortunaCz": "https://www.ifortuna.cz/cz/sazeni/progaming"},
}  # , "ChanceCz":"https://www.chance.cz/kurzy/e-sporty-188" }}
DB_MAPPINGS = {"LoL": "lol", "Dota": "dota", "CS:GO": "csgo"}
GOOGLE_PW = "lcehnmvhakfrzlhr"
LOG_LVL = logging.WARN
DEBUG = False
GMAIL_USER_MAIL = "pavelklammert@gmail.com"


logging.basicConfig(
    filename="run_log.log",
    filemode="a",
    format="%(asctime)s %(name)s - %(levelname)s - %(message)s",
    level=LOG_LVL,
)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    DATABASE_URI = "postgres://postgres:Darthpic0@localhost/"
    IMPLEMENTED_BOOKIES = {"LoL": ["ifortuna"]}
    DB_MAPPINGS = {"LoL": "lol"}
    GOOGLE_PW = "lcehnmvhakfrzlhr"
    LOG_LVL = logging.WARN


class DevelopmentConfig(Config):
    DEBUG = True

    AWS_ACCESS_KEY_ID = "aws-access-key-for-dev"
    AWS_SECERT_ACCESS_KEY = "aws-secret-access-key-for-dev"
    AWS_S3_BUCKET_NAME = "aws-s3-bucket-name-for-dev"

    DATABASE_URI = "database-uri-for-dev"


class TestConfig(Config):
    DEBUG = True
    TESTING = True

    AWS_ACCESS_KEY_ID = "aws-access-key-for-test"
    AWS_SECERT_ACCESS_KEY = "aws-secret-access-key-for-test"
    AWS_S3_BUCKET_NAME = "aws-s3-bucket-name-for-test"

    DATABASE_URI = "database-uri-for-dev"


class ProductionConfig(Config):
    DEBUG = False

    AWS_ACCESS_KEY_ID = "aws-access-key-for-prod"
    AWS_SECERT_ACCESS_KEY = "aws-secret-access-key-for-prod"
    AWS_S3_BUCKET_NAME = "aws-s3-bucket-name-for-prod"

    DATABASE_URI = "database-uri-for-dev"


class CIConfig:
    SERVICE = "travis-ci"
    HOOK_URL = "web-hooking-url-from-ci-service"


# # main.py
# import sys
# import config
#
# ...
#
# if __name__ == '__main__':
#     env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
#
#     if env == 'dev':
#         app.config = config.DevelopmentConfig
#     elif env == 'test':
#         app.config = config.TestConfig
#     elif env == 'prod':
#         app.config = config.ProductionConfig
#     else:
#         raise ValueError('Invalid environment name')
#
#     app.ci = config.CIConfig
