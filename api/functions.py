import json
from flask import jsonify

def execute(dump):
    fdata = json.loads(json.dumps(dump))
    body = list(fdata.values())
    # data = json.dumps(body[1])
    print(dump)