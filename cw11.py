import tripdata 
from datetime import datetime
import json

class trip_details(tripdata.tripdata_store):


    def datetoobject(self):
        date =  datetime.strptime(self.visit_date,"%d %B, %Y")
        return date.strftime("%d %B, %Y")
    def tojson(self):
        return json.dumps(self.details)


user1 = trip_details("Munnar", "15 May, 2023")

print(user1.datetoobject())
print(user1.tojson())

