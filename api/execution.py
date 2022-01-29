import json
from flask import jsonify
from .functions import *
from .misc import *

def backtrace(id, edges):
    inputs = []
    for i in edges:
        if i['target'] == id:
            inputs.append(i)   
            
        # backtrack(i)
    return inputs

# def backtrack(root_i):
#     for k in edges:
#         if (root_i['source'] == k['target']):
#             nid = indexing(k['source'])
#             var= nid.split('_')[0][0]
#             if var =='O':
#                 back_inputs = backtrace(k['source'], edges)
#                 # print(((k['source'].split('_'))[0]), back_inputs, data)
#                 data[k['source']] = (execute(((k['source'].split('_'))[0]), back_inputs, data))
#                 root_inputs.append(k)
#             if var == 'V':
#                 root_inputs.append(k)

def execute(op, input, data):
    # print(data[input[0]['source']])
    # print(data[input[1]['source']])
    # print(op, input, data)
    if op == 'Add':
        res = add(int(data[input[0]['source']]), int(data[input[1]['source']]))
        # print(res)
    elif op == 'Sub':
        res = sub(int(data[input[0]['source']]), int(data[input[1]['source']]))
        
    elif op == 'Mul':
        res = mul(int(data[input[0]['source']]), int(data[input[1]['source']]))
     
    elif op == 'Div':
        res = div(int(data[input[0]['source']]), int(data[input[1]['source']]))
    
    return str(res)
    

def process(dump):
    index = 0
    exec = 0
    fdata = json.loads(json.dumps(dump))
    # body = list(fdata.values())
    # data = json.dumps(body[1])
    # a = dump['body']
    # queue = a['elements']
    # # exec = len(queue)
    # data = a['data']
    # for id in data:
    #     if id=='Output':
    #         print(id)
    # print(queue)
    dump_elements = fdata['body']['elements']
    data = fdata['body']['data']
    elements = []
    edges = []
    root_inputs = []

    
    for i in dump_elements:
        if list(i.keys())[0] == 'id':
            elements.append(i)
        else:
            edges.append(i)
    
    
    for i in edges:
        if i['target'].split('_')[0] == 'Output':
            src = i['source']
    for i in edges:
        if (i['source'] == src):
            root = i 
        
            
    for k in edges:
        if (root['source'] == k['target']):
            nid = indexing(k['source'])
            var= nid.split('_')[0][0]
            if var =='O':
                back_inputs = backtrace(k['source'], edges)
                # print(((k['source'].split('_'))[0]), back_inputs, data)
                data[k['source']] = (execute(((k['source'].split('_'))[0]), back_inputs, data))
                root_inputs.append(k)
            if var == 'V':
                root_inputs.append(k)
    # print(((root['source'].split('_'))[0]), root_inputs, data)
    
    op = execute(((root['source'].split('_'))[0]), root_inputs, data)
    print(op)

    
    return({'elements': elements, 
            'edges': edges, 
            'data': data,
            'root': root,
            'root-inputs': root_inputs,
            'backed-inputs': back_inputs,
            'output': op
            })
    # return op

    
