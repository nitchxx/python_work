import json

class tripdata_store :
    def __init__(self,city_name,visit_comment,visit_date):
        details = {"city_name":city_name,"visit_comment":visit_comment,"visit_date":visit_date}
        self.details = details
        self.visit_date = visit_date
     
    
    def visited_date(self):
       return self.visit_date