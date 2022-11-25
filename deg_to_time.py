#def to_tab(filename):




def deg_to_time(deg):
    hour = deg/15
    minute = (hour - int(hour))*60
    second = round((minute-int(minute))*60,2)
    

    print(str(int(hour))+ " " + str(int(minute)) + " " + str(second))

deg_to_time(-21.78202)