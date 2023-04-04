var = {}

print(var)
print(type(var)) # This is only used to know/check what kind of content is var which os a []

var2 = {"number" : 386}

print(var2)

var2["fruits"] = "apples" # To give a value apples to the key fruits
print(var2)

var2["number"] = 493 # To update a dictionary, we have replaced the value of number here, the reason why dictionaries are more in use bc they provide much more order

print(var2)
print(dir(var))
print(list(var2.keys())) # This is just to print the keys only, no vaolue. See below how to print values:

print(list(var2.values())) # How to print the values
#The beauty of dictionaries is the key-values
# BELOW ISS HOW TO ITERRATE THROUGH DICTIONARIES

for k, v in var2.items():
    print(k, v)  #Lines 24 and 25 are going to be very useful for our usecase.
    

