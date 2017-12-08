import time


def GetWifiTimer():
    #current_time = time.ctime().split(' ')[3]
    current_time ='13:54:21'
    current_hour = int(current_time[:2])
    current_min = current_time[3:5]
    close_min = int(current_min) / 5 + 1
    if close_min == 12 and current_hour != 23:
        close_min = 0
        close_hour = int(current_hour) + 1
        open_hour = close_hour
        open_min = close_min + 1
    elif close_min == 12 and current_hour == 23:
        close_hour = 0
        close_min = 0
        open_hour = close_hour
        open_min = close_min + 1
    else:
        close_hour = int(current_hour)
        open_hour = close_hour
        open_min = close_min + 1
    if open_min == 12 and open_hour != 23:
        open_min = 0
        open_hour += 1
    elif open_min == 12 and open_hour == 23:
        open_hour = 0
        open_min = 0
    else:
        pass

    return [close_hour, close_min, open_hour, open_min]



print GetWifiTimer()

