# let's study how work with json in python

import json


def main():
    json_data = '{"name": "John", "age": "27"}'
    python_json_obj = json.loads(json_data)
    print(python_json_obj)
    print(type(python_json_obj))

    # after parsing json_data we have the dictionary structure
    for key in python_json_obj.keys():
        print(python_json_obj[key])


if __name__ == "__main__":
    main()
