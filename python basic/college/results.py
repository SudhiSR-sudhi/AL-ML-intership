data = {}

def add_mark(sid, score):
    """Saves a student mark."""
    data[sid] = int(score)
    return "Mark saved!"

def get_grade(sid):
    """Gives a Pass/Fail grade based on marks."""
    score = data.get(sid, 0)
    if score >= 40:
        return "Pass"
    return "Fail"

def check_scholarship(sid):
    """Checks if student gets a scholarship (90+ marks)."""
    score = data.get(sid, 0)
    if score >= 90:
        return "Eligible for Scholarship!"
    return "Not eligible for Scholarship."