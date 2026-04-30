from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_PATH = Path(__file__).resolve().parents[3] / "data"
DB_PATH.mkdir(exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH / "game.db"}")
SessionLocal = sessionmaker(engine)

class Base(DeclarativeBase):
    pass