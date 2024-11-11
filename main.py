from math import floor


def time_to_seconds(time):
    """Convert the time entered as a string into seconds."""
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


def seconds_to_time(seconds_count):
    """Convert the time entered in seconds into time format."""
    hours = seconds_count // 3600
    minutes = floor((seconds_count - (hours * 3600)) / 60)
    seconds = seconds_count - (hours * 3600 + minutes * 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    time_format = f"{hours}:{minutes}:{seconds}"
    return time_format


def calculate_pace(time, distance):
    pace_in_seconds = time_to_seconds(time) / distance
    pace = seconds_to_time(pace_in_seconds)
    print(pace_in_seconds)
    print(pace)

print(seconds_to_time(183.9))
calculate_pace("30:39", 10)

# distance_entered = input("Enter the distance in kilometres: ")
# time_entered = input("Enter your time (use format 'h:mm:ss' or 'mm:ss'): ")
# print(time_entered)
# print(time_to_seconds(time_entered))
#
# print(calculate_pace(time_to_seconds(time_entered), distance_entered))

print(seconds_to_time(4128))