import yaml

# List of dictionaries
persons = [{'name': 'Terry', 'age': 34},
           {'name': 'Mike', 'age': 30}]

# It will convert "persons" variable into a YAML node
print(yaml.dump(persons))

# It will output a list of mappings
# '''
# - age: 34
#   name: Terry
# - age: 30
#   name: Mike
# '''