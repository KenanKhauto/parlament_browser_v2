import hashlib
from datetime import datetime, time, timedelta
import re


def compute_hash(value : str):
    '''
    Computes the SHA-256 hash of a string
    @param string: The string to hash
    @return: The hexadecimal representation of the hash
    @raise: TypeError if the string is not a string
    '''
    if not isinstance(value, str):
        raise TypeError("The value must be a string object")
    
    sha256_hash = hashlib.sha256()
    sha256_hash.update(value.encode('utf-8'))
    hash_value = sha256_hash.hexdigest()

    return hash_value

def parse_date_utils(date_string : str, format : str = "%d.%m.%Y"):
    '''
    Parses a date string into a datetime object
    @param date_string: The date string to parse
    @param format: The format of the date string
    @return: The datetime object
    @raise: TypeError if the date_string and format are not strings 
    @raise: ValueError if the time_string is not in the correct
    format
    '''
    if not isinstance(date_string, str):
        raise TypeError("The date_string must be a string object")
    
    if not isinstance(format, str):
        raise TypeError("The format must be a string object")
    
    if len(format) == 0:
        return None
    
    date = datetime.strptime(date_string, format)
    
    return date


def parse_time_utils(time_string : str, format : str = "%H:%M"):
    '''
    Parses a time string into a datetime object
    @param time_string: The time string to parse
    @param format: The format of the time string
    @return: The datetime object
    @raise: TypeError if the time_string is not a string
    @raise: ValueError if the time_string is not in the correct
    format
    '''
    if not isinstance(time_string, str):
        raise TypeError("The time_string must be a string object")
    
    if not isinstance(format, str):
        raise TypeError("The format must be a string object")
    
    if len(format) == 0:
        return None
    
    time = datetime.strptime(time_string, format)
    
    return time

def calculate_duration_in_seconds_utils(start_time, end_time):
    '''
    Calculates the duration between two times in seconds
    @param start_time: The start time
    @param end_time: The end time
    @return: The duration in seconds
    @raise: TypeError if start_time and end_time are not datetime objects
    '''
    if not isinstance(start_time, datetime):
        raise TypeError("The start_time must be a datetime object")
    
    if not isinstance(end_time, datetime):
        raise TypeError("The end_time must be a datetime object")
    

    duration = end_time - start_time

    if duration <= timedelta(seconds=0):
        duration += timedelta(days=1)

    return duration.total_seconds()
   
def beuatify_string(string : str):
    '''
    Beautifies a string
    @param string: The string to beautify
    @return: The beautified string
    @raise: TypeError if the string is not a string
    '''
    if not isinstance(string, str):
        raise TypeError("The string must be a string object")
    
    return " ".join(string.replace("\n", "").replace("\t", "").split())



def remove_numbers_letters(string):
    pattern = r'^\d+\s|\b\d+\b|\b\w(?=\s*\))'
    result = re.sub(pattern, '', string)
    return result.strip()


if __name__ == "__main__":
    # print(compute_hash("Hello World!"))
    # print(parse_date_utils("01.01.2021").date() < parse_date_utils("02.01.2021").date())
    # print(parse_time_utils("21:00") - parse_time_utils("01:00"))
    # start = parse_time_utils("08:00")
    # end = parse_time_utils("08:00")
    
    # print(calculate_duration_in_seconds_utils(start, end) / 60 / 60)
    # test = """BÜNDNIS 90/DIE
    #                     GRÜNEN"""
    # print(beuatify_string(test))
    test = "Beschlussempfehlung und Bericht des Rechtsausschusses (6. Ausschuss)"
    print(remove_numbers_letters(test))
