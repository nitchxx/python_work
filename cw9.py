class vehicle :
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id = _vehicle_id
        self._base_rate = _base_rate

    def display_details(self):
     return f"Vehicle ID: {self._vehicle_id}, Base rate: {self._base_rate}"

    def rental_charge(self) :
        return 0.0

class car(vehicle) :
    def __init__(self, _vehicle_id, _base_rate,num_seats):
        super().__init__(_vehicle_id, _base_rate)
        self.num_seats = num_seats

    def rental_charge(self) :
            return self._base_rate * self.num_seats

class bike(vehicle) :
    def __init__(self, _vehicle_id, _base_rate,bike_type):
        super().__init__(_vehicle_id, _base_rate)
        self.bike_type = bike_type

    def rental_charge(self) :
                return self._base_rate * 0.5
    
def calculate_rental(vehicle):
     return vehicle.rental_charge()


car1 = car( "CAR001",100.0,4)
bike1 = bike("BIKE001",100.0,"Scooter")

print(calculate_rental(car1))
print(calculate_rental(bike1))