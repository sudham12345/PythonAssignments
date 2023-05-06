import json
import jsonschema

def validate(file1,file2):
# read the JSON data from file1
    try:
        with open(file1, 'r') as f:
            data = json.load(f)     
    except ValueError as e:
        print("Malformed JSON data:", e)
        exit()

# read the JSON schema from file2
    try:
        with open(file2, 'r') as f:
          schema = json.load(f)
    except ValueError as e:
        print("Malformed JSON schema:", e)
        exit()

# validate the JSON data against the schema
    try:
        jsonschema.validate(data, schema)
        return True
        #print("JSON data is valid!")
    
    except jsonschema.exceptions.ValidationError as e:
        print("JSON validation error:", e)
    