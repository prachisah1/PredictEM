from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)

    heart_rate = Column(Float)

    blood_pressure = Column(Float)

    oxygen_level = Column(Float)

    injury_severity = Column(Integer)

    triage = Column(String)


engine = create_engine("sqlite:///data/patients.db")

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)