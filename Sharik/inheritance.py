# Inheritence : - 


# class Father:
#                     father_1st_property = "Taj Hotel"

#                     def father_assets(self):
#                          print("Bhardwaj aprament")
#                          print("Willing Restaurant")


# father_obj =  Father() 

# print(father_obj.father_1st_property)
# father_obj.father_assets()





# class Father:
#                     father_1st_property = "Taj Hotel"

#                     def father_assets(self):
#                          print("Bhardwaj aprament")
#                          print("Willing Restaurant")

# class Son:
#                     son_1st_property = "minee restaurant"


# son_obj = Son()

# print(son_obj.son_1st_property)


# Single Inheritence : -

# => in this case , a child class inherits properties and methods from a single parent class.

# class Father:
#                     father_1st_property = "Taj Hotel"

#                     def father_assets(self):
#                          print("Bhardwaj aprament")
#                          print("Willing Restaurant")

# class Son(Father):
#                     son_1st_property = "minee restaurant"

# son_obj = Son()

# print(son_obj.son_1st_property)
# print(son_obj.father_1st_property)
# son_obj.father_assets()



# there are two types of class 

# 1. Parent class ( base class , super class)

# => the class whose properties and methods are inheritey by child class is called parent class.



# 2. Child class ( derived class , sub class)

# => the class which inherits properties and methods from parent class is called child class.



# multiple Inheritence : -

=> in this case, a child can inherit more than one parent class.

class GrandFather:
             grandfather_1st_property = "Grand HOtel"

             def grandfather_assets(self):
                    print("deliscious dishes")
                    print("APna Restaurant")


class Father:
                    father_1st_property = "Taj Hotel"

                    def father_assets(self):
                         print("Bhardwaj aprament")
                         print("Willing Restaurant")

class Son(GrandFather, Father):
                    son_1st_property = "minee restaurant"

son_obj = Son()

print(son_obj.grandfather_1st_property)
print(son_obj.father_1st_property)
print(son_obj.son_1st_property)
son_obj.grandfather_assets()
son_obj.father_assets()


Water 
american acent


Liberia  


