from math import floor, ceil
from running_pace import pace_10km, pace_ANP


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
    hours = int(seconds_count // 3600)
    minutes = floor((seconds_count - (hours * 3600)) / 60)
    seconds = seconds_count - (hours * 3600 + minutes * 60)
    if type(seconds) is float:
        seconds = round(seconds, 1)
    time_format = ""
    if seconds < 10:
        if hours == 0:
            time_format = f"{minutes}:0{seconds}"
        elif hours > 0 and minutes < 10:
            time_format = f"{hours}:0{minutes}:0{seconds}"
        elif hours > 0 and minutes > 9:
            time_format = f"{hours}:{minutes}:0{seconds}"
    else:
        if hours == 0:
            time_format = f"{minutes}:{seconds}"
        elif hours > 0 and minutes < 10:
            time_format = f"{hours}:0{minutes}:{seconds}"
        elif hours > 0 and minutes > 9:
            time_format = f"{hours}:{minutes}:{seconds}"
    return time_format


def calculate_pace(distance, time):
    pace_in_seconds = ceil(time_to_seconds(time) / distance)
    pace = (seconds_to_time(pace_in_seconds))
    return pace


# This function can be used if the pace is calculated with an accuracy on 1/10s (not used ceil() in calculate_pace() or
# if the format of distance should be e.g. "1,5 km", not "1.5 km".
def replacing_dot_to_comma(text):
    text = str(text)
    text_with_comma = text.replace(".", ",")
    return text_with_comma


def find_index(pace):
    """Find an index of a current pace in the proper list or the first faster pace in the proper list."""
    if pace in pace_10km:
        return(pace_10km.index(pace))
    else:
        while pace not in pace_10km:
            pace = time_to_seconds(pace) - 1
            pace = seconds_to_time(pace)
        return pace_10km.index(pace)


distance_entered = float(input("Enter the distance in kilometres: "))
time_entered = input("Enter your time (use format 'h:mm:ss' or 'mm:ss' or 'm:ss'): ")
print(f"Distance: {replacing_dot_to_comma(distance_entered)} km")
if len(time_entered) > 5:
    print(f"Time: {time_entered} h")
else:
    print(f"Time: {time_entered} min")

print(f"Your pace is {(calculate_pace(distance_entered, time_entered))} minutes per kilometer.")

pace_10km_index = find_index(calculate_pace(distance_entered, time_entered))

print(f"Your ANP pace is {pace_ANP[pace_10km_index]} minutes per kilometer.")
