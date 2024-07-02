import mysql.connector as sql
from termcolor import colored
def show(flight):
    db = sql.connect(host='localhost' , user='root' , password='' , database='flight')
    cursor = db.cursor()
    action = True if flight.action == "LANDING" else False
    print(colored("Flight Number :" , 'blue') , f"{colored(flight.flight_number , 'green' if action else 'red')}")
    print(f"{colored(flight.plane , 'blue')} {colored('LANDED from' if action else 'TOOK OFF to' , 'green' if action else 'red')} {colored(flight.city , 'blue')}")
    print(colored(f"{flight.action} in {flight.datetime}" , 'green' if action else 'red'))
    query = f"INSERT INTO `log` (`flight_id`,`flight_number`,`city`,`plane`,`action`,`fly_date`) VALUES ('','{flight.flight_number}' , '{flight.city}' , '{flight.plane}' , '{flight.action}' , '{flight.datetime}')"
    cursor.execute(query)
    db.commit()

def showdelay(flight , delay):
    action = True if flight.action == "LANDING" else False
    print(colored(f"Flight Number {flight.flight_number} {flight.plane}", 'yellow') , colored(flight.action , 'green' if action else 'red') , colored(f"{flight.datetime} DELAYED for {delay} minutes" , 'yellow'))