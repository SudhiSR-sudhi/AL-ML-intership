members_data = {}

def add_member(member_id, name):
    
    members_data[member_id] = name
    return "Member registered successfully!"

def get_member(member_id):
    return members_data.get(member_id, "Member not found")

def count_members():   
    return len(members_data)