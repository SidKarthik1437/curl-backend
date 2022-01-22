import json
from flask import jsonify
from .functions import * 



def execute(dump):
    index = 0
    exec = 0
    fdata = json.loads(json.dumps(dump))
    body = list(fdata.values())
    # data = json.dumps(body[1])
    a = dump['body']
    queue = a['queue']
    exec = len(queue)
    data = a['data']
    print(queue)
    print(data)
    
    
    for op in queue:
        if 'Add' in op:
            res, index = add(int(data[index]), int(data[index+1]), index)
            print(res)
            print(index)
        elif 'Sub' in op:
            res, index = sub(int(data[index]), int(data[index+1]), index)
            print(res)
            print(index)
        elif 'Multiply' in op:
            res, index = mul(int(data[index]), int(data[index+1]), index)
            print(res)
            print(index)
        elif 'Divide' in op:
            res, index = div(int(data[index]), int(data[index+1]), index)
            print(res)
            print(index)


