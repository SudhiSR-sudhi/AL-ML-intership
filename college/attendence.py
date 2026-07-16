# Storage for attendance percentages
data = {}

def add_attendance(sid, percentage):
    """Saves attendance percentage."""
    data[sid] = int(percentage)
    return "Attendance saved!"

def check_exam_ok(sid):
    """Checks if attendance is 75% or higher."""
    score = data.get(sid, 0)
    if score >= 75:
        return f"Allowed! Attendance is {score}%"
    return f"Blocked! Attendance is only {score}%"