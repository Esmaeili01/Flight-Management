import mysql.connector as sql
from random import randint
from datetime import datetime 
class Flight:  
    def __init__(self , now):
        self.db = sql.connect(host='localhost' , user='root' , password='' , database='flight')
        self.cursor = self.db.cursor()
        self.now = now
    def __str__(self):
        return str (self.flight_number) + " " + str(self.city) + " " + str(self.plane) + " " + str(self.datetime) + " " + str(self.action)
    def select(self):
        self.plane_selector()
        self.city_selector()
        self.flight_number_selector()
        self.action_selector()
        self.datetime_selector()
        return  self.datetime_object
       
    def flight_number_selector(self):
         while True:
            self.flight_number = randint(1000 , 9999)
            result = self.check(self.flight_number)
            if result == 0:
                break
            else:
                pass
    def city_selector(self):
        self.cursor.execute("SELECT city_name FROM city")
        cities = self.cursor.fetchall()
        self.city = cities[randint(0,len(cities)-1)][0]
    def plane_selector(self):
        self.cursor.execute("SELECT plane_name FROM plane")
        planes = self.cursor.fetchall()
        self.plane = planes[randint(0,len(planes)-1)][0]
    def datetime_selector(self):
        hour = day = month = year = 0
        minute = randint(0,20) + self.now.minute
        if minute >= 60:
            minute %= 60
            hour = 1
        hour += self.now.hour
        if hour >= 24:
            hour %= 24
            day = 1
        day += self.now.day
        if day > 30 :
            day = 1
            month = 1
        month += self.now.month
        if month > 12:
            month = 1
            year = 1
        year += self.now.year    
        self.datetime_object = datetime(year , month , day , hour , minute , 0)
        self.year = year
        self.month = month        
        self.day = day
        self.hour = hour
        self.minute = minute
        self.date = f"{year}/{month}/{day}"
        self.time = f"{hour}:{minute}"
        self.datetime = f"{self.date} {self.time}"
    def retiming(self):
        self.datetime_object = datetime(self.year , self.month , self.day , self.hour , self.minute , 0)
        self.date = f"{self.year}/{self.month}/{self.day}"
        self.time = f"{self.hour}:{self.minute}"
        self.datetime = f"{self.date} {self.time}"
    def action_selector(self):
        action = ["TAKE-OFF" , "LANDING"]
        self.action = action[randint(0,1)]
    def check(self , num):
        self.cursor.execute(f"SELECT fly_date FROM log WHERE flight_number={num} ORDER BY flight_id DESC")
        temp = self.cursor.fetchall()
        if len(temp) == 0:
            return 0
        else : 
            result = temp[0][0]
            fly_date = datetime(int(result[:4]), int(result[5:7]) , int(result[8:]))
            if self.now.year == fly_date.year and self.now.month == fly_date.month and self.now.day == fly_date.day:
                return 1
            else:
                return 0
    def __del__(self):
        pass