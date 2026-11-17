class Employee :
    def __init__(self,name,role):
        self.name = name 
        self.role = role

    def display(self):
        print("Name : ",self.name,"\n","Role : ",self.role)

class Trainer(Employee) :
    def __init__(self, name, role,specialization,**kwargs):
        self.specialization = specialization
        super().__init__(name, role,**kwargs)

    def display(self):
            print("Name : ",self.name,"\n","Role : ",self.role,"\n","Specilization : ",self.specialization)

class YogaInstructor(Employee) :
     def __init__(self, name, role,yoga_style ,**kwargs):
          self.yoga_style =yoga_style 
          super().__init__(name, role,**kwargs)

     def display(self):
                print("Name : ",self.name,"\n","Role : ",self.role,"\n","yoga_style : ",self.yoga_style)

class Multi_trainer(Trainer,YogaInstructor) :
    def __init__(self, name, role, specialization,yoga_style):
         super().__init__(name = name,role = role,specialization = specialization,yoga_style = yoga_style)

    def display(self):
                print("Name : ",self.name,"\n","Role : ",self.role,"\n","Specilization : ",self.specialization,"\n","yoga_style : ",self.yoga_style)

multitrainer1 = Multi_trainer("Anjali","Basic trainer","Yoga specialist , Gym trainer","Hatha Yoga")
multitrainer1.display()