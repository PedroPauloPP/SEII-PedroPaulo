#my module
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Encontra o indice de um item'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1