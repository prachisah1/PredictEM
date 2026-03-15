from fastapi import FastAPI
from pydantic import BaseModel

from fastapi import Depends
from sqlalchemy.orm import Session
from modules.database import get_db
from modules.models import TriageModel
from modules.data_processing import load_data, preprocess
from modules.allocation import allocate_resources
from modules.database import SessionLocal, save_patient
from modules.routing import find_nearest_hospital
from modules.caching import get_cache, set_cache
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------- TRAIN MODEL ON STARTUP --------

data = load_data("data/mock_patient_data.csv")

X, y = preprocess(data)

model = TriageModel()

model.train(X, y)

# --------------------------------------


class Patient(BaseModel):
    heart_rate: float
    blood_pressure: float
    oxygen_level: float
    injury_severity: int


@app.post("/triage")
async def triage(patient: Patient, db: Session = Depends(get_db)):

    cache_key = f"{patient.heart_rate}_{patient.blood_pressure}_{patient.oxygen_level}_{patient.injury_severity}"

    cached = get_cache(cache_key)

    if cached:
        return {"triage_category": cached, "source": "cache"}

    patient_data = [
        patient.heart_rate,
        patient.blood_pressure,
        patient.oxygen_level,
        patient.injury_severity
    ]

    result = model.predict(patient_data)

    set_cache(cache_key, result)

    save_patient(db, patient_data, result)

    return {"triage_category": result, "source": "model"}

@app.post("/allocate-resources")
async def allocate(patients: list[Patient]):

    return allocate_resources(patients)

@app.get("/dispatch-ambulance")
async def dispatch():

    result = find_nearest_hospital()

    return result