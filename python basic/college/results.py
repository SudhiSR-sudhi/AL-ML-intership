data = {}

def add_mark(sid, score):
    data[sid] = int(score)
    return "Mark saved!"

def get_grade(sid):
    score = data.get(sid, 0)
    if score >= 40:
        return "Pass"
    return "Fail"

def check_scholarship(sid):
    score = data.get(sid, 0)
    if score >= 90:
        return "Eligible for Scholarship!"
    return "Not eligible for Scholarship."