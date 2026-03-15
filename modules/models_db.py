from sqlalchemy import Column, Integer, Float, String
from modules.base import Base


class PatientRecord(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    heart_rate = Column(Float)

    blood_pressure = Column(Float)

    oxygen_level = Column(Float)

    injury_severity = Column(Integer)

    triage_category = Column(String)