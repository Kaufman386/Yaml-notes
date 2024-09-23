import YAML

# Open file in read mode
with open("parsing.yaml", "r") as stream:
    try:
        # When we deserialize python, we allow external document to enter python application. So we used safe_load since that is risky
        print(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(e)

# When you run this file, it will parse `parsing.yaml` file and outpute:
# {'groceries': ['bananas', 'oatmeal', 'milk', 'eggs']}