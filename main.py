from Queue import Queue
from datetime import datetime
from ongoing import ongoing
from time import sleep
from termcolor import colored
from newtime import newtime , checkForNext
from show import showdelay
takeoff = Queue()
landing = Queue()
now = datetime.now()
while True:

    now = ongoing(takeoff , landing , now)

    takeoffHour = takeoff.array[takeoff.front].hour
    takeoffMinute = takeoff.array[takeoff.front].minute
    landingHour = landing.array[landing.front].hour
    landingMinute = landing.array[landing.front].minute
    
    if takeoffHour == landingHour:
        if takeoffMinute <= landingMinute:
            if takeoffMinute + 5 > landingMinute:
                checkForNext(landing)
                showdelay(takeoff.display() , landingMinute - takeoffMinute + 5)
                takeoff.array[takeoff.front].minute = landingMinute + 5
                newtime(takeoff)
            else:
                checkForNext(takeoff)
        else:
            if landingMinute + 5 > takeoffMinute:
                checkForNext(landing)
                showdelay(takeoff.display() , landingMinute - takeoffMinute + 5)
                takeoff.array[takeoff.front].minute = landingMinute + 5
                newtime(takeoff)
            else :
                checkForNext(landing)
    elif (takeoffHour + 1)%24 == landingHour : 
        if takeoffMinute <= landingMinute:
            checkForNext(takeoff)
        else:
            if takeoffMinute + 5 > landingMinute + 60:
                checkForNext(landing)
                showdelay(takeoff.display() , landingMinute - takeoffMinute + 65 )
                takeoff.array[takeoff.front].minute = landingMinute + 5
                newtime(takeoff)
            else:
                checkForNext(takeoff)
    elif (landingHour + 1)%24 == takeoffHour:
        if landingMinute <= takeoffMinute:
            checkForNext(landing)
        else:
            if landingMinute + 5 > takeoffMinute + 60:
                checkForNext(landing)
                showdelay(takeoff.display() , landingMinute - takeoffMinute - 55)
                takeoff.array[takeoff.front].minute = landingMinute + 5
                newtime(takeoff)
            else:
                checkForNext(landing)
    elif (takeoffHour + 1)%24 < landingHour:
        checkForNext(takeoff)
    elif (landingHour + 1)%24 < takeoffHour:
        checkForNext(landing)
    else:
        pass
    print(colored("-----------------------------" , 'cyan'))
    sleep(1)