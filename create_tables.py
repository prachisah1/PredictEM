from modules.database import engine
from modules.base import Base
from modules.models_db import PatientRecord

Base.metadata.create_all(bind=engine)

print("Tables created successfully")