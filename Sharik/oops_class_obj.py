
class => A class is a blueprint or template used to create objects.

=> A class is a blueprint that defines the properties (attributes) and behavior (methods) of objects in object-oriented programming.

class Student:

              student_name = "Wilmot"
              email = "wilmot@example.com"
              __atm_pin = 1234 # private variable

              def student_info(self):
                    print("Student name is :", self.student_name)
                    print("Student email is :", self.email)

object_student = Student()   

print(object_student.student_name)  # wilmot
print(object_student.email)

object_student.student_info() # first method to call a function


my_functon = object_student.student_info
my_functon()    # second method to call  a funciton 




# if there are some real time objects ( teachers, students, desks, chairs, WHiteboard etc) are avilable in any room , in that case only You can say it is just like a classroom.



object => it is an instance of a class, that contines real world entity. 
=> it is just like a collection of variables and methods.



object_student = Student()  
in this above line , object_student is an object of class Student.

=> object_student is just like a variable that holds all properties and methods of class Student.
