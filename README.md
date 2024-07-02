# Flight-Management
Flight management with Circular Queue data structure \
We have two Queues , one for Take-offs and one for Landings. \
The minimum time interval between flights is 5 minutes. \
Landing takes priority over take-off. \
so if there are a take-off at 19:00 and a landing at 19:03 , the take-off flight must wait untill 19:08 (19:03 + 00:05). \
Since this is a simulation , we use random numbers and names. \

The Python libraries we need : 
- mysql
- random
- datetime
- termcolor (for a better look)

Import the **flight.sql** to your mysql database.We need a database to hold city and plane names and log. \
Put all the python files on the same directory and run the **main.py**.\
the result will be in Terminal and the log table on flight database.
