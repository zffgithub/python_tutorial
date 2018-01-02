#!/usr/bin/env python
#coding: utf-8
import json

def run():
    data = {"spam": "foo", "parrot": 42}
    in_json = json.dumps(data)  # Encode the data
    print type(in_json), in_json
    to_json = json.loads(in_json)  # Decode into a Python object
    print type(to_json), to_json

if __name__ == "__main__":
    run()
        