from modules.data_generator import generate_patient_data

df = generate_patient_data(1000)

df.to_csv("data/mock_patient_data.csv", index=False)

print("Dataset Generated Successfully!")