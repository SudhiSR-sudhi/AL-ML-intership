patient_data = {}

def add_patient(pid, name):
    patient_data[pid] = name
    return "patient added!"

def get_patient(pid):
    return patient_data.get(pid, "Not found")

def count_patient():
    return len(patient_data)
