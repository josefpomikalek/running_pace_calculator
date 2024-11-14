from math import floor


paces = {
    "p_1500m" : "4:33",
    "p_3km" : "4:45",
    "p_5km" : "4:58",
    "p_10km" : "5:18",
    "p_anp" : "5:27",
    "p_end3" : "5:37",
    "p_mar" : "5:44",
    "p_end2" : "6:00",
    "p_end1" : "6:49",
    "p_rec" : "7:16"
}

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
    pace_in_seconds = time_to_seconds(time) / distance
    pace = seconds_to_time(pace_in_seconds)
    return pace


def replacing_dot_to_comma(text):
    text = str(text)
    text_with_comma = text.replace(".", ",")
    return text_with_comma


distance_entered = float(input("Enter the distance in kilometres: "))
time_entered = input("Enter your time (use format 'h:mm:ss' or 'mm:ss' or 'm:ss'): ")
print(f"Distance: {replacing_dot_to_comma(distance_entered)} km")
if len(time_entered) > 5:
    print(f"Time: {time_entered} h")
else:
    print(f"Time: {time_entered} min")

print(f"Your pace is {replacing_dot_to_comma(calculate_pace(distance_entered, time_entered))} minutes per kilometer.")
