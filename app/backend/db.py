from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создаем движок для SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///taskmanager.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Создаем локальную сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)