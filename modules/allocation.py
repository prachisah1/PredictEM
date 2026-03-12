from pulp import LpMaximize, LpProblem, LpVariable


def allocate_resources(patients):

    model = LpProblem("Hospital_Allocation", LpMaximize)

    beds = LpVariable("beds", lowBound=0)
    doctors = LpVariable("doctors", lowBound=0)

    model += beds + doctors

    model += beds <= 50
    model += doctors <= 20

    model.solve()

    return {
        "beds": beds.value(),
        "doctors": doctors.value()
    }