patients_data = {}

def add_patient(pid, name):
    patients_data[pid] = name
    return "patient added!"

def get_patient(pid):
    return patients_data.get(pid, "Not found")

def count_patient():
    return len(patients_data)
