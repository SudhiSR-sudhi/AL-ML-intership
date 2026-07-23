doctors_data = {}

def add_doctor(did, name):
    doctors_data[did] = name
    return "doctor added!"

def get_doctor(did):
    return doctors_data.get(did, "Not found")

def count_doctors():
    return len(doctors_data)
