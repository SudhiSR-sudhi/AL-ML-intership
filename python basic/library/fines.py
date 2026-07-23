

fines_data = {}

def apply_fine(fine_id, member_id, amount):
    from library.members import members_data as m_db
    if member_id not in m_db:
        return "Error: Member ID not found!"
        
    fines_data[fine_id] = {"member_id": member_id, "amount": amount, "status": "Unpaid"}
    return "Fine recorded successfully!"

def pay_fine(fine_id):
    if fine_id in fines_data:
        fines_data[fine_id]["status"] = "Paid"
        return "Fine payment cleared successfully!"
    return "Error: Fine record not found!"
