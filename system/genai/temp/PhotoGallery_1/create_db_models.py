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


class User(Base):\n    """description: This table stores user details."""\n    __tablename__ = 'users'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    username = Column(String, nullable=False)\n    email = Column(String, nullable=True)\n    registered_on = Column(DateTime, nullable=True)


class Photograph(Base):\n    """description: This table stores photograph details, including their uploader."""\n    __tablename__ = 'photographs'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    title = Column(String, nullable=False)\n    upload_date = Column(DateTime, nullable=True)\n    uploaded_by_user_id = Column(Integer, ForeignKey('users.id'))\n    image_path = Column(String, nullable=False)


class Category(Base):\n    """description: This table maintains categories for organizing photographs."""\n    __tablename__ = 'categories'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(String, nullable=True)


class PhotoCategory(Base):\n    """description: This is a junction table linking photographs and categories."""\n    __tablename__ = 'photo_categories'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    photo_id = Column(Integer, ForeignKey('photographs.id'))\n    category_id = Column(Integer, ForeignKey('categories.id'))


class Comment(Base):\n    """description: This table stores comments made by users on photographs."""\n    __tablename__ = 'comments'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    photograph_id = Column(Integer, ForeignKey('photographs.id'))\n    user_id = Column(Integer, ForeignKey('users.id'))\n    content = Column(Text, nullable=False)\n    comment_date = Column(DateTime, nullable=True)


class Tag(Base):\n    """description: This table holds tags associated with photographs."""\n    __tablename__ = 'tags'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)


class PhotoTag(Base):\n    """description: This is a junction table linking photographs and tags."""\n    __tablename__ = 'photo_tags'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    photo_id = Column(Integer, ForeignKey('photographs.id'))\n    tag_id = Column(Integer, ForeignKey('tags.id'))


class Notification(Base):\n    """description: This table stores notifications sent to users."""\n    __tablename__ = 'notifications'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    message = Column(String, nullable=False)\n    is_read = Column(Boolean, default=False)\n    sent_date = Column(DateTime, nullable=True)


class Favorite(Base):\n    """description: This table records user favorites on photographs."""\n    __tablename__ = 'favorites'\n\n    id = Column(Integer, primary_key=True, autoIncrement=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    photo_id = Column(Integer, ForeignKey('photographs.id'))


class Album(Base):\n    """description: This table represents photo albums created by users."""\n    __tablename__ = 'albums'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    description = Column(String, nullable=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    created_date = Column(DateTime, nullable=True)


class AlbumPhotograph(Base):\n    """description: This is a junction table linking photographs and albums."""\n    __tablename__ = 'album_photographs'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    album_id = Column(Integer, ForeignKey('albums.id'))\n    photo_id = Column(Integer, ForeignKey('photographs.id'))


class Follower(Base):\n    """description: This table manages user follow relations."""\n    __tablename__ = 'followers'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    user_id = Column(Integer, ForeignKey('users.id'))\n    follower_id = Column(Integer, ForeignKey('users.id'))


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    user_1 = User(id=1, username="john_doe", email="john@example.com", registered_on=date(2023, 1, 10))
    user_2 = User(id=2, username="jane_doe", email="jane@example.com", registered_on=date(2023, 2, 15))
    user_3 = User(id=3, username="alex_smith", registered_on=date(2023, 3, 18))
    user_4 = User(id=4, username="lisa_brown")
    photo_1 = Photograph(id=1, title="Sunset", upload_date=date(2023, 5, 15), uploaded_by_user_id=1, image_path="/images/sunset.jpg")
    photo_2 = Photograph(id=2, title="Mountains", upload_date=date(2023, 6, 20), uploaded_by_user_id=2, image_path="/images/mountains.jpg")
    photo_3 = Photograph(id=3, title="Beach", upload_date=date(2023, 7, 3), uploaded_by_user_id=1, image_path="/images/beach.jpg")
    photo_4 = Photograph(id=4, title="Cityscape", upload_date=date(2023, 8, 22), uploaded_by_user_id=3, image_path="/images/cityscape.jpg")
    category_1 = Category(id=1, name="Nature", description="Photos from nature.")
    category_2 = Category(id=2, name="Urban", description="City and urban landscapes.")
    category_3 = Category(id=3, name="Travel", description="Travel photography.")
    category_4 = Category(id=4, name="Black and White", description="Monochrome pictures.")
    photo_category_1 = PhotoCategory(id=1, photo_id=1, category_id=1)
    photo_category_2 = PhotoCategory(id=2, photo_id=2, category_id=3)
    photo_category_3 = PhotoCategory(id=3, photo_id=3, category_id=1)
    photo_category_4 = PhotoCategory(id=4, photo_id=4, category_id=2)
    comment_1 = Comment(id=1, photograph_id=1, user_id=2, content="Amazing photo!", comment_date=date(2023, 5, 16))
    comment_2 = Comment(id=2, photograph_id=2, user_id=1, content="Great capture!", comment_date=date(2023, 6, 21))
    comment_3 = Comment(id=3, photograph_id=3, user_id=3, content="Beautiful view.", comment_date=date(2023, 7, 4))
    comment_4 = Comment(id=4, photograph_id=4, user_id=4, content="Love the skyline.", comment_date=date(2023, 8, 23))
    
    
    
    session.add_all([user_1, user_2, user_3, user_4, photo_1, photo_2, photo_3, photo_4, category_1, category_2, category_3, category_4, photo_category_1, photo_category_2, photo_category_3, photo_category_4, comment_1, comment_2, comment_3, comment_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
