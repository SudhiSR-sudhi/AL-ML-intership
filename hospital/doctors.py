data = {}

def add_doctor(did, name):
    data[did] = name
    return "patient added!"

def get_doctor(did):
    return data.get(did, "Not found")

def count_doctors():
    return len(data)
