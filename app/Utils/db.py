import os
import databases
import ormar
import sqlalchemy
from sqlalchemy import DateTime
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from app.config import settings

generalPosrgresBase = databases.Database(settings.generalPosrgres)
generalPosrgresMetadata = sqlalchemy.MetaData()

class generalPosrgres(ormar.ModelMeta):
    metadata = generalPosrgresMetadata
    database = generalPosrgresBase

class User(ormar.Model):
    class Meta(generalPosrgres):
        tablename = "user"
    name:            str = ormar.Text(max_length=255, nullable=True)
    email:           str = ormar.Text(max_length=255, primary_key=True)
    password:        str = ormar.Text(max_length=255, nullable=True)
    created:         str = ormar.Text(max_length=255, nullable=True)
    roles:           str = ormar.Text(max_length=255, nullable=True)

class Foot(ormar.Model):
    class Meta(generalPosrgres):
        tablename = "foot"
    number:          int = ormar.Integer(minimal=0, primary_key=True)
    name:            str = ormar.Text(max_length=255, nullable=True)
    price:           int = ormar.Integer(minimal=0, nullable=True)
    description:     str = ormar.Text(max_length=255, nullable=True)
    active:          bool = ormar.Boolean()

class Order(ormar.Model):
    class Meta(generalPosrgres):
        tablename = "order"
    created:         str = ormar.Text(max_length=255, nullable=True)
    sum:             int = ormar.Integer(minimal=0, nullable=True)
    number:          int = ormar.Integer(minimal=0, primary_key=True)
    description:     str = ormar.Text(max_length=255, nullable=True)
    status:          str = ormar.Text(max_length=255, nullable=True)
    positions:       str = ormar.Text(max_length=1024, nullable=True)


engine = sqlalchemy.create_engine(settings.generalPosrgres)
generalPosrgresMetadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()