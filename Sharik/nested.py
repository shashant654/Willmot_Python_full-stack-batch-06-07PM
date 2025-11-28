# Example: Checking age and citizenship for voting eligibility

# age = int(input("Enter your age: "))

# citizen = input("Are you an Indian citizen? (yes/no): ")

# if age >= 18:

#     if citizen.lower() == "yes":
#         print("You are eligible to vote in India.")
#     else:
#         print("You must be an Indian citizen to vote.")


# else:
#     print("You must be at least 18 years old to vote.")





# task : write a program to check if a person is eligible for voting


age = int(input("Hii GUYS! Enter your age: "))

if age >= 18 :

        print("yes , you are eligible to vote")
     
else: 
     print("you are not eligigble to vote")




age = int(input("Hii GUYS! Enter your age: "))

citizen = input("enter your citizership: ")

if age >= 18 :

        if citizen == "indian":
           print("yes , you are eligible to vote")
        else:
           print("sorry, you must be an Indian to vote")
     
else: 
     print("you are not eligigble to vote")

