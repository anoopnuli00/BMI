"""
usage: python main.py

1. This script takes input_json with person info
2. Calculates BMI
3. Generates output report
"""

import json
import jsonschema
import os
import pandas as pd
from data.code.input_code import Code as SchemaCode
from settings import BMI

def validating_json_with_schema(json_data, schema_path: str):
    '''
    open json schema file to validate the input config json file
    '''

    try:
        # load schema
        with open(os.path.abspath(schema_path)) as schema_file:
            schema = json.loads(schema_file.read())
        try:
            # validate the json input and schema
            jsonschema.validate(json_data, schema)

        except jsonschema.ValidationError as error:
           print('Validation with schema failed -  {}'.format(error.message))
           return False

        except jsonschema.SchemaError as error:
            print('Schema Error -  {}'.format(error))
            return False

    except OSError as error:
        print(f"Json Schema file not found in path {schema_path}")
        return False

    return True

def calculate_bmi(height, weight, json_object):
    ''' to calculate bmi and generate result'''

    bmi_params = BMI()

    current_bmi = (weight/(height*height)) * 10000

    for ele in bmi_params.bmi_dict.values():
        lower_bound = ele[0]
        upper_bound = ele[1]

        if(lower_bound <= current_bmi <= upper_bound):
            json_object["BMI"] = current_bmi
            json_object["BMI Category"] = ele[2]
            json_object["Health Risk"] = ele[3]
            return json_object


if __name__ == "__main__":

    output = []

    # json schema path
    json_schema_path = "data/schema/input_schema.json"

    # open input_json data
    try:
        with open("input.json") as f:
            input_json = json.load(f)
    except json.decoder.JSONDecodeError as error:
        print(f"{error}")
        exit()

    for key, json_object in input_json.items():
        # validate input json file with json schema
        if(validating_json_with_schema(json_object, json_schema_path)):

            # load json data into code
            schema_code = SchemaCode.from_dict(json_object)

            if(schema_code.height_cm > 0 and schema_code.weight_kg >0):

                output.append(calculate_bmi(height=schema_code.height_cm, weight=schema_code.weight_kg, json_object=json_object))

    with open('output.txt', "w") as f:
        f.write(str(output))