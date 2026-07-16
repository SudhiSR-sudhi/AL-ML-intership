

billing_data = {}

def create_bill(bill_id, patient_id, amount):
    from hospital.patients import patients_data as p_db
    if patient_id not in p_db:
        return "Error: Patient not found!"
        
    billing_data[bill_id] = {
        "patient_id": patient_id,
        "amount": amount,
        "status": "Unpaid"
    }
    return "Bill generated!"

def pay_bill(bill_id):

    if bill_id in billing_data:
        billing_data[bill_id]["status"] = "Paid"
        return "Payment successful!"
    return "Bill not found"
