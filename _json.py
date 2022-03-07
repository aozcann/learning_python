
# dict




# person = {"name" : "Ali" , "languages" : ["Python","c#"] }

# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

import json


person_string = '{"name" : "Ali" , "languages" : ["Python","c#"] }'
person_dict = {"name" : "Ali","languages" : ["Python","C#"]}

#JSON string to Dict
# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]


# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])



# Dict to JSON string

# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# write in person.json
# with open("person.json","w") as f:
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict , indent=4, sort_keys=True)
print(person_dict)
print(result)