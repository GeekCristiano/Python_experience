# let's study how work with json in python

import json


def main():
    json_data = '{"name": "John", "age": "27"}'
    python_obj = json.loads(json_data)
    print(python_obj)
    print(type(python_obj))


if __name__ == "__main__":
    main()
