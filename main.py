
def time_to_seconds(time):

    """Transfer the time entered as a string to seconds"""
    if len(time) == 8:  # For the time format hh:mm:ss
        hours = int(time[:2])
        minutes = int(time[3:5])
        seconds = int(time[6:])
    elif len(time) == 7:    # For the time format h:mm:ss
        hours = int(time[:1])
        minutes = int(time[2:4])
        seconds = int(time[5:])
    elif len(time) == 4:    # For the time format mm:ss
        hours = 0
        minutes = int(time[:1])
        seconds = int(time[2:])
    else:   # For the time format m:ss
        hours = 0
        minutes = int(time[:2])
        seconds = int(time[3:])
    time_in_seconds = hours * 3600 + minutes * 60 + seconds
    return time_in_seconds


def calculate_pace(time, distance):
    pace = float(time / int(distance))
    return pace


distance_entered = input("Enter the distance in metres: ")
time_entered = input("Enter your time (use format 'h:mm:ss' or 'mm:ss'): ")
print(time_entered)
print(time_to_seconds(time_entered))

