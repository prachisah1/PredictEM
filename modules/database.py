from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.models_db import PatientRecord

DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def save_patient(db, patient_data, triage):

    record = PatientRecord(
        heart_rate=patient_data[0],
        blood_pressure=patient_data[1],
        oxygen_level=patient_data[2],
        injury_severity=patient_data[3],
        triage_category=triage
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record