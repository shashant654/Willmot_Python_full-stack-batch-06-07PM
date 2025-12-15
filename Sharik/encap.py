# class Bank:
      
#       bank_name = "SBI"
#       account_number = "167886766"
#       bank_balance = "10000000"

#       def Wilmmot_bank_information(my):
#                     print("bank name :", my.bank_name)
#                     print("account_number",my.account_number)
#                     print("bank balance :", my.bank_balance)

# bank_obj  = Bank()

# print(bank_obj.bank_name)
# bank_obj.Wilmmot_bank_information()


# ----------------------------------------------------

# class Wilmot_Bank:
      
#       bank_name = "SBI"
#       _account_number = "167886766"
#       __bank_balance = "10000000"
#       __atm_pin = "7878"


#       def Wilmmot_bank_information(my):
#                     print("bank name :", my.bank_name)
#                     print("account_number",my._account_number)
#                     print("bank balance :", my.__bank_balance)

# bank_obj  = Wilmot_Bank()

# print(bank_obj.bank_name)
# bank_obj.Wilmmot_bank_information()
# print(bank_obj._account_number)
# # print(bank_obj.__bank_balance)  # it gives error



# there are 3 access specifier:

# public => no any type of prefix => bank_name = "SBI"
# protected("_")  => single underscore such like prefix =>  _bank_balance = "10000000"
# private ("__")  => Double Underscore such prefix =>  __atm_pin = "7878"

# 1. Public => it can be accessible anywhere .

# 2. Protected => it can be accessible inside the class , but python give access to access protected members outside the class also.

# 3. Private => it can be accessible only inside the class , not outside the class .



# ----------------------------------------------------------------

# class Wilmot_Bank:
      
#       bank_name = "SBI"
#       _account_number = "167886766"
#       __bank_balance = "10000000"
#       __atm_pin = "7878"


#       def __Wilmmot_bank_information(my):
#                     print("bank name :", my.bank_name)
#                     print("account_number",my._account_number)
#                     print("bank balance :", my.__bank_balance)

# bank_obj  = Wilmot_Bank()

# print(bank_obj.bank_name)

# bank_obj.__Wilmmot_bank_information()

# -------------------------------------------------------------------


class Wilmot_Bank:
      
      bank_name = "SBI"
      _account_number = "167886766"
      __bank_balance = "10000000"
      __atm_pin = "7878"


      def _Wilmmot_bank_information(my):
                    print("bank name :", my.bank_name)
                    print("account_number",my._account_number)
                    print("bank balance :", my.__bank_balance)

bank_obj  = Wilmot_Bank()

print(bank_obj.bank_name)

bank_obj._Wilmmot_bank_information()

