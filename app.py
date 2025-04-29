from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
engine = create_engine("sqlite:///app.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


# Create tables
Base.metadata.create_all(engine)

# Example usage
if __name__ == "__main__":
    db = Session()

    # Create
    new_user = User(name="John Doe", email="john@example.com")
    db.add(new_user)
    db.commit()

    # Read
    users = db.query(User).all()
    print("Users:")
    for user in users:
        print(f"- {user.name} ({user.email})")
