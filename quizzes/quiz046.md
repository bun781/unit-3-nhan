# Paper Code
![image](https://github.com/user-attachments/assets/2c8231f9-21bb-4235-b6fd-b14c6bfc2de6)

# Code
```.py
class Citizen:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    def getName(self):
        return self.name
    def getCity(self):
        return self.city
    def getStatus(self):
        return self.status

class Employee(Citizen):
    def __init__(self, name, city, status, annual_salary):
        Citizen.__init__(self, name=name,city=city,status=status)
        self.annual_salary=annual_salary
    def getAnnualSalary(self):
        return self.annual_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, annual_salary, fraction, union):
        Employee.__init__(self, name=name,city=city,status=status,annual_salary=annual_salary)
        self.fraction = fraction
        self.union = union

a = PartTimeEmployee('hi', 'hi' ,'hi', 1000, 0.8, False)
print(a.getAnnualSalary(), a.getName(), a.getStatus(), a.getCity())
```

# Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/a6d58146-6065-4252-ad6d-a77e32a4bc9d" />
