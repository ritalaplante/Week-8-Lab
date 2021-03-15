# Dictionaries
# Helpful resource for going over the basics:
# https://www.w3schools.com/python/python_dictionaries.asp

# Declaring an empty dictionary:
capitals = {}

# Adding items to a dictionary

capitals["Massachusetts"] = "Boston"
capitals["California"] = "Sacramento"
capitals["Hawaii"] = "Honolulu"

print(capitals)

capitals.update({"New York" : "Albany"})

print(capitals)

# Update can also be used to replace pre-existing keys

capitals.update({"New York" : "New York City"})

print(capitals)

# ...and you can change them using braket notation
capitals["New York"] = "Albany"

# Accessing items in a dictionary braket notation
massCap = capitals["Massachusetts"]

# Accessing items in a dictionary using get notation
massCap = capitals.get("Massachusetts")

# To get a list of the keys in a dictionary
states = capitals.keys()
print(states)

# Now you try...
# Define your own dictionary. Write a function that takes in a dictionary and a
# key. Check if the key is in your dictionary. If it is, return the value
# associated with that key. If not return "key not found."

# Looping through dictionaries:
# return all the values in a dictionary

for k in capitals:
    print(capitals[k])

# Loop through with key value pairs

for k, v in capitals.items():
    print(k, v)

