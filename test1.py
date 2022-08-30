me = {
    "f_name": "Eduardo",
    "l_name": "Reynoso Rosales",
    "color": "black",
    "hobbies": [],
    "address": {"number": 147, "street": "Vets", "city": "Tijuana"},
}

# get data from the dictionary
print(me["f_name"] + "" + me["l_name"])

# modify
me["color"] = "white"

# add
me["age"] = 18

# read non existing key
# -------------print(me["title"])

# check if a key exist inside a dictionary
if "title" in me:
    print(me["title"])

# print things in addres
address = me["address"]
print(address["street"] + " " + str(address["number"]) + " " + address["city"])
