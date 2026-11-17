class person :
    def __init__(self,name,age,**kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def show_details(self):
              print("My name is {}. I am {} years old.".format(self.name,self.age))
class employee(person) :
     def __init__(self,name,age,employee_id,**kwargs):
          self.employee_id = employee_id
          super().__init__(name,age,**kwargs)
          


     def show_details(self):
      print("My name is {}. I am {} years old. ID ={}".format(self.name,self.age,self.employee_id))

class parttime(person) :
     def __init__(self, name, age,working_hours,**kwargs):
          self.working_hours = working_hours
          super().__init__(name, age,**kwargs)
          
        
     def show_details(self):
        print("My name is {}. I am {} years old. working hours = {}".format(self.name,self.age,self.working_hours))

class consultant(employee,parttime):
      def __init__(self, name, age, employee_id,working_hours,project_name):
            self.project_name = project_name
            super().__init__(name = name,age = age,employee_id = employee_id,working_hours = working_hours)
            

      def show_details(self):
        print("My name is {}. I am {} years old. Employee_id : {} , working hours : {} , project_name : {}".format(self.name,self.age,self.employee_id,self.working_hours,self.project_name))

employee1 = consultant("Abhiraj",23,"FE248",5.40,"Hospital_website")
employee1.show_details()

