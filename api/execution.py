import json
from typing import Type
from flask import jsonify
from numpy import equal
from .functions import *
from .misc import *

elements = []
edges = []
flow = {}
outputs = []
inputs = {}
values = {}
finals = {}

# def backtrace(id, edges):
#     inputs = []
#     for i in edges:
#         if i['target'] == id:
#             inputs.append(i)

#         # backtrack(i)
#     return inputs


def findEle(id):
    global elements
    for i in elements:
        if i['id'] == id:
            return i


def backtrack(i):
    global flow, elements, edges, outputs, inputs
    op = i
    inputs.update({op['id']: []})
    for j in edges:
        #! output[id] == edge['target]
        if op['id'] == j['target']:
            # print("op", j)
            flow.update({op['id']: []})
            if (indexing(j['source'])).split('_')[0] == 'O':
                # print(j['source'])
                flow[op['id']].append((j['source']))
                inputs[op['id']].append(j['source'])

            elif (indexing(j['source'])).split('_')[0] == 'V':
                if j['source'] == None:
                    return
                else:
                    # print(j['source'])
                    inputs[op['id']].append(j['source'])
            for k in elements:
                if k['id'] == j['source']:
                    backtrack(k)


def executions(id, data, op):
    global flow, elements, edges, outputs, inputs, finals
    for i in inputs[id]:
        if indexing(i).split('_')[0] == 'O':
            finals.update({i: {'value': executions(i, data, i.split('_')[0])}})
        else:
            return execute(inputs[id], data, op)
    # else:
    #     execute(inputs)


def execution(ip, data, op):
    global flow, elements, edges, outputs, inputs, finals
    if type(ip) == str:
        return
    else:
        for i in ip:
            if indexing(i).split('_')[0] == 'O':
                finals.update(
                    {i: {'value': execution(i, data, i.split('_')[0])}})
            else:
                return execute(ip, data, op)


def execute(input, data, op):
    # print(data[input[0]])
    # print(data[input[1]])
    # print('op', op)
    res = 0
    if op == 'Add':
        for i in input:
            res += float(data[i])
            # print("hehe", i)
        # print(res)
    elif op == 'Sub':
        res = sub((data[input[0]]), (data[input[1]]))

    elif op == 'Mul':
        res = mul((data[input[0]]), (data[input[1]]))

    elif op == 'Div':
        res = div((data[input[0]]), (data[input[1]]))

    return str(res)


def process(dump):

    global flow, elements, edges, outputs, inputs, finals
    # flow = []
    # outputs = []
    # inputs = []
    index = 0
    exec = 0
    fdata = json.loads(json.dumps(dump))
    # region Data Dump
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
    # endregion
    dump_elements = fdata['body']['elements']
    data = fdata['body']['data']
    for i in dump_elements:
        if list(i.keys())[0] == 'id':
            elements.append(i)
        else:
            edges.append(i)

    #! Calculating Outputs
    for i in elements:
        if ((i['id']).split('_'))[0] == 'Output':
            outputs.append(i)
            flow.update({i['id']: []})

    for i in outputs:
        backtrack(i)

    for i in flow:
        # print(i, inputs[i])
        if len(inputs[i]) == 1:
            # print(i)
            if inputs[i][0] in inputs:
                executions(inputs[i][0], data, (i.split('_'))[0])
        # if len(inputs[i]) > 1 :
        #     execution(inputs[i], data, (i.split('_'))[0])
        else: 
            for i in inputs[i]:
                print('i')
                # executions(i[0], data, (i.split('_'))[0])
        
        
    print(finals)
    return flow, inputs, data


# for k in elements:
#                    #! element[id] == edge[source]
#                    if k['id'] == j['source']:
#                         flow[i['id']].append(k['id'])
#                         print("new source: ", k)
#                         op = flow[i['id']][-1]
#                     print('new op:', op)
