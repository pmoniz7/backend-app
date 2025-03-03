import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

#SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['DATABASE_USER']}:@{os.environ['DATABASE_HOST']}/{os.environ['DATABASE_NAME']}"

##user = os.environ['DATABASE_USER']
##password = os.environ['DATABASE_PASSWORD']
##host = os.environ['DATABASE_HOST']
##port = os.environ['DATABASE_PORT']
##db_name = os.environ['DATABASE_NAME']

##SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
##SQLALCHEMY_DATABASE_URL = f'postgresql://mybase_qnof_user:wyIA3t2wq2f4JC90tzM9ftsp0YegJ1Bj@dpg-curk442n91rc73ct4jc0-a:5432/mybase_qnof'

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

print("<<<<< SQLALCHEMY_DATABASE_URL >>>>> ", SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

print("<<<<< engine  >>>>> ", engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()