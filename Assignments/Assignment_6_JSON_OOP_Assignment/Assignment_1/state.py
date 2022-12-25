import json
	
# Data to be written
State_Capital = {
    "Maharastra" : "Mumbai",
    "Gujrat" : "Gandhinagar",
    "Madhya Pradesh": "Bhopal",
    "Karnataka" : "Bangalore",
    "Bihar": "Patna",
    "Goa": "Panaji",
    "Chattisghar": "Naya Raipur",
}

#  Wtrite data from dictionary to json file
with open("sample.json", "w") as file:
    json.dump(State_Capital, file)