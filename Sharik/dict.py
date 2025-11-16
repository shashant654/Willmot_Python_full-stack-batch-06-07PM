# Dictionary — Definition

# A dictionary in Python is mutable, and key–value pair collection.
# It allows you to store and retrieve data using keys, instead of numeric indexes.

Dictionary is ordered data structure.


# # name , age , department, and data are keys
# => Sharik, 19 , Cse , 1111111 => these are values
my_dict = {
                    "name": "Sharik",
                    "age" : 19,
                    "department": "CSE",
                    "data" : "11111111111"
}

print(my_dict["name"])  # Sharik

print("before changes", my_dict)

my_dict["name"] = "WIlmot"
print("after changes ", my_dict)

my_dict["country"] = "India"
print("after adding one more field", my_dict)

my_dict["city"] = "Meerut"
print("after adding city", my_dict)

my_dict.pop("city")
print("after removing city", my_dict)




# my_name = "sharik"
# print(my_name)


# my_listt = [11,33,44,55]
# print(my_listt[3])  # 55