import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    email = Column(String(256))
    password = Column(String(256))

class Favorites(Base):
    __tablename__= "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer)
    
class Characters(Base):
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    hair_color = Column(String(256))
    eye_color = Column(String(256))
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(256))
    birth_year = Column(String)
    skin_color = Column(String)

class Planets(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(256))
    gravity = Column(String(256))
    terrain = Column(String(256))
    surface_water = Column(Integer)
    population = Column(Integer)

class Vehicles(Base):
    __tablename__="vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    model = Column(String(256))
    manufacturer = Column(String(256))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(256))
    vehicle_class = Column(String(256))



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
