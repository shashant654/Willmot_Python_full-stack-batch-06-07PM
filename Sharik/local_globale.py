# global varible and Local variable ?

1. Global variable => a varialb which is declared outside the function or class is called global variable.
=> it can be accessed anywhere in the program.

2. Local variable => a variable which is declared inside the function or class is called local variable.
=> it can be accessed only inside the function or class.

Trainer = "Shashant"  ## global varible

def total_students():
                    std_class = "BCA"  # local variable

                    print("WIlmot")
                    print("SHarik")
                    print("Aakansha")

                    print(std_class)
total_students()

print(Trainer)
print(std_class)  # error  because std_class is local variable