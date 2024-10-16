from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


class SessionConfig():
    def __init__(self):
        ...

    def url(self):
        db_user = 'postgres'
        db_pass = 'postgres'
        db_host = 'localhost'
        db_port = 5432
        db_name = 'db_posts'
        return f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


session_config = SessionConfig()
engine = create_engine(session_config.url())
Session = sessionmaker(bind=engine)
