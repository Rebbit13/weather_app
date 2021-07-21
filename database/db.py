import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{db}".format(
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('APP_DB_HOST'),
    port=os.getenv('POSTGRES_PORT'),
    db=os.getenv('POSTGRES_DB')
)

os.environ['DATABASE_URL'] = SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()


Session = sessionmaker()
Session.configure(bind=engine)
