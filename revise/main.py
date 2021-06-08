users = {
    "rohit":{
        "name": "Rohit",
        "City": "Berlin",
        "Age": 33,
        "Job": "DevOps Engineer",
    },
    "binsha":{
        "name": "Binsha",
        "City": "Kerala",
        "Age": 28,
        "Job": "Home Maker"
    }
}

print(users["rohit"]["Age"])  # Prints 33

for user,value in users.items(): #.items to iterate over key value pair
    #print(user) # Prints each user in separate line
    if user == "rohit":
        print(value)

for value in users.values(): # iterate over values
    if value["Age"] < 30:
        print(value["name"])


for key in users.keys(): # iterate over values
    if key == "binsha":
        
        print(key.get("Job"))