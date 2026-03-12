from fastapi import FastAPI
from pydantic import BaseModel

from modules.models import TriageModel
from modules.data_processing import load_data, preprocess
from modules.allocation import allocate_resources


app = FastAPI()

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
def triage(patient: Patient):

    patient_data = [
        patient.heart_rate,
        patient.blood_pressure,
        patient.oxygen_level,
        patient.injury_severity
    ]

    result = model.predict(patient_data)

    return {"triage_category": result}


@app.post("/allocate-resources")
def allocate(patients: list[Patient]):

    return allocate_resources(patients)