import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}@database:{port}/{db}".format(
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    port=os.getenv('POSTGRES_PORT'),
    db=os.getenv('POSTGRES_DB')
)
print(SQLALCHEMY_DATABASE_URL)

os.environ['DATABASE_URL'] = SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()


Session = sessionmaker()
Session.configure(bind=engine)
