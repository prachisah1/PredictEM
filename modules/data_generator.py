import pandas as pd
import random

def generate_patient_data(n=1000):

    data = []

    for _ in range(n):

        heart_rate = random.randint(60, 180)
        blood_pressure = random.randint(60, 160)
        oxygen_level = random.randint(75, 100)
        injury_severity = random.randint(1, 5)

        # TRIAGE RULES
        if oxygen_level < 85 or injury_severity >= 4:
            triage = "Red"

        elif heart_rate > 120 or injury_severity == 3:
            triage = "Yellow"

        else:
            triage = "Green"

        data.append([
            heart_rate,
            blood_pressure,
            oxygen_level,
            injury_severity,
            triage
        ])

    df = pd.DataFrame(
        data,
        columns=[
            "heart_rate",
            "blood_pressure",
            "oxygen_level",
            "injury_severity",
            "triage_category"
        ]
    )

    return df