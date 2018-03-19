# let's study how work with json in python

import json


def main():
    # from json to python
    json_data = '{"name": "John", "age": "27"}'
    python_json_obj = json.loads(json_data)
    print(python_json_obj)
    print(type(python_json_obj))

    # after parsing json_data we have the dictionary structure
    for key in python_json_obj.keys():
        print(python_json_obj[key])

    # from python to json
    python_json_obj = {"name": "John", "age": 27, "isEmployee": True}
    json_data = json.dumps(python_json_obj)
    print(json_data)


if __name__ == "__main__":
    main()
