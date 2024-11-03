
def time_to_seconds(time):

    """Transfer the time entered as a string to seconds"""
    minutes = int(time[:2])
    seconds = int(time[3:])
    time_in_seconds = minutes * 60 + seconds
    return time_in_seconds


time_entered = input("Enter your time (use format 'h:mm:ss' or 'mm:ss'): ")
print(time_entered)
print(time_to_seconds(time_entered))