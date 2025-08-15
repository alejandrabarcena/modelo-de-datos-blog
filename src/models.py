import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)  # no exponer en serialize
    first_name = Column(String(80))
    last_name = Column(String(80))
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    favorite_planets = relationship("FavoritePlanet", back_populates="user", cascade="all, delete-orphan")
    favorite_characters = relationship("FavoriteCharacter", back_populates="user", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
        }

class Planet(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False, index=True)
    climate = Column(String(120))
    terrain = Column(String(120))
    population = Column(String(120))
    gravity = Column(String(80))
    diameter = Column(String(80))
    rotation_period = Column(String(80))
    orbital_period = Column(String(80))

    fans = relationship("FavoritePlanet", back_populates="planet", cascade="all, delete-orphan")
    residents = relationship("Character", back_populates="homeworld")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "gravity": self.gravity,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
        }

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False, index=True)
    gender = Column(String(40))
    birth_year = Column(String(40))
    height = Column(String(40))
    mass = Column(String(40))
    hair_color = Column(String(40))
    skin_color = Column(String(40))
    eye_color = Column(String(40))

    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    homeworld = relationship("Planet", back_populates="residents")
    fans = relationship("FavoriteCharacter", back_populates="character", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "homeworld_id": self.homeworld_id,
        }

class FavoritePlanet(Base):
    __tablename__ = "favorite_planets"
    __table_args__ = (UniqueConstraint("user_id", "planet_id", name="uq_user_planet"),)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="favorite_planets")
    planet = relationship("Planet", back_populates="fans")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "created_at": self.created_at.isoformat(),
        }

class FavoriteCharacter(Base):
    __tablename__ = "favorite_characters"
    __table_args__ = (UniqueConstraint("user_id", "character_id", name="uq_user_character"),)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="favorite_characters")
    character = relationship("Character", back_populates="fans")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "created_at": self.created_at.isoformat(),
        }

# Genera el diagrama ER a partir de los modelos
try:
    render_er(Base, "diagram.png")
    print("diagram.png generado ✅")
except Exception as e:
    print("ERROR generando diagrama:", e)
