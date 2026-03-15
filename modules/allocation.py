from pulp import LpProblem, LpMaximize, LpVariable, lpSum

def allocate_resources(patients):

    num_patients = len(patients)

    # optimization model
    model = LpProblem("Hospital_Resource_Allocation", LpMaximize)

    # decision variables
    beds = LpVariable("beds", lowBound=0)
    doctors = LpVariable("doctors", lowBound=0)
    ventilators = LpVariable("ventilators", lowBound=0)

    # objective: maximize resource utilization
    model += beds + doctors + ventilators

    # constraints
    model += beds <= 100
    model += doctors <= 40
    model += ventilators <= 20

    # solve
    model.solve()

    return {
        "patients_received": num_patients,
        "beds_allocated": beds.value(),
        "doctors_allocated": doctors.value(),
        "ventilators_allocated": ventilators.value()
    }