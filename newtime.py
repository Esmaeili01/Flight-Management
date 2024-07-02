from show import show , showdelay
def newtime(flight):
    minute = flight.array[flight.front].minute
    hour = day = month = year = 0
    if minute >= 60 :
        minute %= 60
        hour += 1
    flight.array[flight.front].minute = minute
    hour += flight.array[flight.front].hour
    if hour >= 24 :
        hour %= 24
        day += 1 
    flight.array[flight.front].hour = hour
    day += flight.array[flight.front].day
    if day > 30 :
        day %= 30
        month += 1
    flight.array[flight.front].day = day
    month += flight.array[flight.front].month
    if month > 12 : 
        month %= 12
        year += 1
    flight.array[flight.front].month = month
    flight.array[flight.front].year += year
    flight.array[flight.front].retiming() 

def checkForNext(flights):
    flight1 = flights.array[flights.front]
    flight2 =  flights.array[(flights.front+1)%flights.Size]
    flight1_hour = flight1.hour 
    flight1_minute = flight1.minute
    flight2_hour = flight2.hour
    flight2_minute = flight2.minute
    show(flight1)
    flights.remove()
    if flight1_hour == flight2_hour:
        if flight1_minute <= flight2_minute:    
            if flight1_minute + 5 > flight2_minute:
                showdelay(flight2 , flight1_minute - flight2_minute + 5 )
                flights.array[flights.front].minute = flight1_minute + 5
                newtime(flights)
            else:
                pass
        else: 
            showdelay(flight2 , flight1_minute - flight2_minute + 5 )
            flights.array[flights.front].minute = flight1_minute + 5
            newtime(flights)
    elif (flight1_hour + 1)%24 == flight2_hour :
        if flight1_minute <= flight2_minute:
            pass
        else:
            if flight1_minute + 5 > flight2_minute + 60:
                showdelay(flight2 , flight1_minute - flight2_minute + 65 )
                flights.array[flights.front].minute = flight1_minute + 5
                newtime(flights)
            else:
                pass
    elif flight1_hour > flight2_hour:
        showdelay(flight2 , ((flight1_hour - flight2_hour)%24)*60 + flight1_minute - flight2_minute +  5 )
        flights.array[flights.front].minute = flight1_minute + 5
        newtime(flights)
    else:
        pass