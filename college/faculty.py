data = {}

def add_teacher(tid, name):
    """Saves a new teacher."""
    data[tid] = name
    return "Teacher added!"

def get_teacher(tid):
    """Finds a teacher by ID."""
    return data.get(tid, "Not found")