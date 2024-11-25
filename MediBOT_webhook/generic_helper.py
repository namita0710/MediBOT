import re
from datetime import datetime, time
from enum import Enum
from dateutil import parser as date_parser

class Appintment_typeList(Enum):
    a = 1
    b = 2
    c = 3
    d = 4

def findAppointmentType_id(appointment_type):
    for item in Appintment_typeList:
        if item.name == appointment_type:
            return item.value
    return None

def merge_date_and_time(date_str, time_str):
    """
    Merge a date string and a time string into a single datetime object.
    
    Parameters:
        date_str (str): The date string.
        time_str (str): The time string.
    
    Returns:
        datetime.datetime: The merged datetime object.
    """
    date_obj = date_parser.parse(date_str).date()
    time_obj = datetime.strptime(time_str, "%H:%M").time()
    return datetime.combine(date_obj, time_obj)


def get_str_from_health_issue_list(health_issue_list: list):
    result = ", ".join(health_issue_list)
    return result

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(0)
        return extracted_string
    return ""

