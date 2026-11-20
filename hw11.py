import tracker
from datetime import datetime
import json 

class trip_details(tracker.tripdata_store):


      def datetoobject(self):
            date =  datetime.strptime(self.visit_date,"%d %B, %Y")
            return date.strftime("%B %d, %Y")
      
      def tojson(self):
            return json.dumps(self.details)

      def toparse(self):
            parseobj = json.loads(self.tojson())
            return parseobj

user1 = trip_details("Munnar", "Enjoyed the tea gardens", "15 May, 2023")
user2 = trip_details("Wayanad", "Visited waterfalls and enjoyed trekking", "20 June, 2024")
user3 = trip_details("Alleppey", "Enjoyed the houseboat experience", "10 January, 2025")

print(user1.datetoobject())
print(user2.datetoobject())
print(user3.datetoobject())

print(user1.tojson())
print(user2.tojson())
print(user3.tojson())

print(user1.toparse())
print(user2.toparse())
print(user3.toparse())



