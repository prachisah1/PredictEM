from modules.data_processing import load_data, preprocess
from modules.models import TriageModel

data = load_data("data/mock_patient_data.csv")

X, y = preprocess(data)

model = TriageModel()

model.train(X, y)