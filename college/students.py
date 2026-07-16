data = {}

def add_student(sid, name):
    """Saves a new student."""
    data[sid] = name
    return "Student added!"

def get_student(sid):
    """Finds a student by ID."""
    return data.get(sid, "Not found")

def count_students():
    """Counts total students."""
    return len(data)