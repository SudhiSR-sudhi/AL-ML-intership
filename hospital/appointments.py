
appointments_data = {}

def add_appointment(apt_id, patient_id, doctor_id, date, time):

    from hospital.patients import patients_data as p_db
    from hospital.doctors import doctors_data as d_db

    if patient_id not in p_db:
        return "Error: Patient not found!"
    if doctor_id not in d_db:
        return "Error: Doctor not found!"
        
    for apt in appointments_data.values():
        if apt["doctor_id"] == doctor_id and apt["date"] == date and apt["time"] == time:
            return "Error: Doctor is busy at this time!"
            
    appointments_data[apt_id] = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }
    return "Appointment scheduled!"

def get_appointment(apt_id):
    return appointments_data.get(apt_id, "Appointment not found")
