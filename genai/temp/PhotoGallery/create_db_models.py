# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Photograph(Base):
    """description: Table to store information about photographs."""
    __tablename__ = 'photograph'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    upload_date = Column(Date, nullable=True)
    photographer_id = Column(Integer, ForeignKey('photographer.id'))
    album_id = Column(Integer, ForeignKey('album.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    category_id = Column(Integer, ForeignKey('category.id'))


class Photographer(Base):
    """description: Table to store information about photographers."""
    __tablename__ = 'photographer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    biography = Column(String, nullable=True)


class Album(Base):
    """description: Table to store information about albums."""
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    creation_date = Column(Date, nullable=True)


class Location(Base):
    """description: Table to store information about photograph locations."""
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


class Category(Base):
    """description: Table to store information about photograph categories."""
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    photograph_1 = Photograph(title='Sunset Bliss', description='A beautiful sunset view', upload_date=date(2023, 9, 10), photographer_id=1, album_id=1, location_id=1, category_id=1)
    photograph_2 = Photograph(title='Mountain Adventure', description='Ascending the peaks', upload_date=date(2023, 8, 5), photographer_id=2, album_id=2, location_id=2, category_id=2)
    photograph_3 = Photograph(title='Urban Exploration', description='Night lights', upload_date=date(2023, 7, 15), photographer_id=1, album_id=3, location_id=3, category_id=3)
    photograph_4 = Photograph(title='Calm Waters', description='Meditative landscapes', upload_date=date(2023, 10, 1), photographer_id=3, album_id=1, location_id=4, category_id=4)
    
    
    
    session.add_all([photograph_1, photograph_2, photograph_3, photograph_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
