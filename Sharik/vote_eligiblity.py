

# Check for vot eligiblity

age = int(input("enter your age"))

citizen = "indian"

if age >= 18:
          if citizen == 'indian':
                    print("You are eligible to vote")
          else:
                    print("YOu must be an indian citizen to vote")

else: 
                    print("you are not eligible to vote")


age = int(input("enter your age"))
citizen = input("enter your citizenship")
if age >= 18:
          if citizen.lower() == 'indian':
                    print("You are eligible to vote")
          else:
                    print("YOu must be an indian citizen to vote")

else: 
                    print("you are not eligible to vote")


# NOte: whenever you have to check more than two conditions, then you should use Nested if or elif .