# Write a script using the json module to read a JSON file and 
#convert it into a Python dictionary.

# importing the module
import json

# Opening JSON file
with open("C:/Users/iTA/Desktop/demo.json") as json_file:
    data = json.load("C:/Users/iTA/Desktop/demo.json")

    # for reading nested data [0] represents
    # the index value of the list
    print(data['people1'][0])
    
    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['people1']:
        print("Name:", i['name'])
        print("Website:", i['website'])
        print("From:", i['from'])
        print()

