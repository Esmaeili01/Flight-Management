from flightselector import Flight
from Queue import Queue
from datetime import datetime

def ongoing(takeoff , landing , now):
    while not (takeoff.full() and landing.full()):
        flight = Flight(now)
        nowtemp = flight.select()
        if flight.action == "LANDING":
            if landing.insert(flight):
                now = nowtemp  
        else:
            if takeoff.insert(flight):
                now = nowtemp
                 
    return now