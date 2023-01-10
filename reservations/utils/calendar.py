import datetime
from calendar import Calendar

def months(start: datetime, end: datetime):
    return ((m_y // 12, (m_y % 12) + 1) for m_y in
            range(12 * start.year + start.month - 1, 12 * end.year + end.month))

def prepare_lessons_dict(start: datetime, end: datetime):
    calendar = Calendar(firstweekday=0)
    lessons = {}
    for (year, month) in months(start, end):
        temp = calendar.monthdatescalendar(year, month)
        temp = [{ day.day if day.month == month else 100 + day.day:[] for day in week} for week in temp]
        
        lessons[(year, month)] = temp
    
    return lessons