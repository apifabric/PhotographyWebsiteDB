# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 21, 2024 20:03:57
# Database: sqlite:////tmp/tmp.8zBKgaKhu6-01JFND15VZEV5ZQ4Y1ABVJHRVB/PhotoGallery/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Album(SAFRSBaseX, Base):
    """
    description: Table to store information about albums.
    """
    __tablename__ = 'album'
    _s_collection_name = 'Album'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creation_date = Column(Date)

    # parent relationships (access parent)

    # child relationships (access children)
    PhotographList : Mapped[List["Photograph"]] = relationship(back_populates="album")



class Category(SAFRSBaseX, Base):
    """
    description: Table to store information about photograph categories.
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PhotographList : Mapped[List["Photograph"]] = relationship(back_populates="category")



class Location(SAFRSBaseX, Base):
    """
    description: Table to store information about photograph locations.
    """
    __tablename__ = 'location'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PhotographList : Mapped[List["Photograph"]] = relationship(back_populates="location")



class Photographer(SAFRSBaseX, Base):
    """
    description: Table to store information about photographers.
    """
    __tablename__ = 'photographer'
    _s_collection_name = 'Photographer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    biography = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PhotographList : Mapped[List["Photograph"]] = relationship(back_populates="photographer")



class Photograph(SAFRSBaseX, Base):
    """
    description: Table to store information about photographs.
    """
    __tablename__ = 'photograph'
    _s_collection_name = 'Photograph'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    upload_date = Column(Date)
    photographer_id = Column(ForeignKey('photographer.id'))
    album_id = Column(ForeignKey('album.id'))
    location_id = Column(ForeignKey('location.id'))
    category_id = Column(ForeignKey('category.id'))

    # parent relationships (access parent)
    album : Mapped["Album"] = relationship(back_populates=("PhotographList"))
    category : Mapped["Category"] = relationship(back_populates=("PhotographList"))
    location : Mapped["Location"] = relationship(back_populates=("PhotographList"))
    photographer : Mapped["Photographer"] = relationship(back_populates=("PhotographList"))

    # child relationships (access children)
