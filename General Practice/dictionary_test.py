from unittest.util import three_way_cmp


dictionary = {
    "con1": ("Shondrell", "47", "married"),
    "con2": ("Theodore", "22", "married"),
    "con3": ("Taquiqui", "ageless", "married")
}

#print(dictionary["age"])
#print(dictionary["name"])

try:
    for entry in dictionary:
        entry = input("Whoose a contestant: ")
        if entry == entry:
            print(dictionary[entry])
except:
    print("Please enter valid entry.")
    