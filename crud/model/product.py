# -*- coding: utf-8 -*-
"""Product model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, Float
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from crud.model import DeclarativeBase, metadata, DBSession


class Product(DeclarativeBase):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(16), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    created = Column(DateTime, default=datetime.now)


__all__ = ['Product']
