v = ['Integer', 'Float', 'Char', 'Bool', 'String']

def indexing(id):
    if any(val in id for val in v):
        return ('V_' + id)
    else:
        return ('O_' + id)