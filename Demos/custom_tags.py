import yaml


# Creates python dictionary for us that matches the YAML node
def constructor(loader, node):
    fields = loader.construct_mapping(node)
    return Person(**fields)


# Add Constructor to YAML and sepcify tag that we'd like to use for it
yaml.add_constructor('!Person', constructor)


class Person(object):

    # ALL instance variables must match the node variables in the YAML file
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # If the names and number of variables in YAML file don't match the ones in our class, we will get an error
        # Look at custom_tags.yaml file for an example ^^


with open("custom_tags.yaml", "r") as stream:
    try:
        # Have to use `unsafe_load` because we are uing custom tags/types
        dict_person = yaml.unsafe_load(stream)
        print(dict_person)
        # Grab the value from the "person" key in the dict_person mapping
        person = dict_person["person"]
        print(person.name, person.age)
    except yaml.YAMLError as e:
        print(e)
    

# This will print out:
# '''
# {'person': <__main__.Person object at 0xSomeAddres>}
# Mike 30
# '''