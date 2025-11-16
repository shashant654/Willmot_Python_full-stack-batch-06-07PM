# Example: Checking age and citizenship for voting eligibility

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")

if age >= 18:
    if citizen.lower() == "yes":
        print("You are eligible to vote in India.")
    else:
        print("You must be an Indian citizen to vote.")
else:
    print("You must be at least 18 years old to vote.")
