#!/usr/bin/python
class Employee:
	'Common base class for employees'
	empcount=0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empcount +=1

	def displayCount(self):
		print("Total Employee: %d" %Employee.empcount)

	def displayEmployee(self):
		print ("Name : ", self.name, ", Salary: ", self.salary)

'First object of emloyee class'
emp1 = Employee("Somanna",20000)
'Second object of employee class'
emp2 = Employee("Maramma",30000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total employee %d" %Employee.empcount)

'Function to manipulate or access attributes'
emp1.age= 29

hasattr(emp1, 'age')
getattr(emp1, 'age')
setattr(emp1, 'age',32)

print("************ Employee Details ****************\n")
print("Name: ",emp1.name, ", Salary: ", emp1.salary, ", Age: ", emp1.age)

