from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql+psycopg2://practice_rw:your_password@localhost/practice_data'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)