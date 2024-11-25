import re
from enum import Enum
from datetime import datetime
from dateutil import parser as date_parser

class Appointment_typeList(Enum):
    a = 1
    b = 2
    c = 3
    d = 4
    
def findAppointmentType_id(appointment_type):
    for item in Appointment_typeList:
        if item.name == appointment_type:
            return item.value   

# def merge_date_and_time(date_obj, time_obj):
#     return datetime.combine(date_obj, time_obj)
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

if __name__ == "__main__":
    # print(findAppointmentType_id("b"))
    date_str = "28-04-2024"  # Sample date string
    time_str = "11:00"   # Sample time string

    merged_datetime = merge_date_and_time(date_str, time_str)
    print("Merged DateTime:", merged_datetime)
