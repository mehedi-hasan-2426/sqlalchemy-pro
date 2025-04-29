from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Base, User
import pytest

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_creation(db_session):
    user = User(name="Test User", email="test@example.com")
    db_session.add(user)
    db_session.commit()
    
    result = db_session.query(User).first()
    assert result.name == "Test User"
    assert result.email == "test@example.com"
