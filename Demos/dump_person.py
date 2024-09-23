import yaml


# Create custom tag (!Person) which is just a Person class in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Assign the variables for our instance
person = Person('Mike', 30)
# dump and print the outcome
dump_person = yaml.dump(person)
print(dump_person)

# Code will output
# '''
# !!python/object:__main__.Person           This is the custom tag (which says it is of type "Python Object Class: Person")
# age: 30
# name: Mike
# '''