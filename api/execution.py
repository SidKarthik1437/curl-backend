import json
from flask import jsonify
from .functions import * 

index = 0

def execute(dump):
    fdata = json.loads(json.dumps(dump))
    body = list(fdata.values())
    # data = json.dumps(body[1])
    a = dump['body']
    queue = a['queue']
    data = a['data']
    print(queue)
    print(data)
    
    global index
    
    for op in queue:
        if 'Add' in op:
            res, index = add(int(data[index]), int(data[index+1]), index)
            print(res)
            print(index)
