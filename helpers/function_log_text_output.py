def deconstruct_arguments(**kwargs):
    return_entity = ''
    for k,v in kwargs.items():
        return_entity += str(type(v))
    return return_entity
    
def call_function(function_name,**kwargs):
    print(f'{function_name.__name__}({deconstruct_arguments(**kwargs)}) fn started')
    function_name(**kwargs)
    print(f'{function_name.__name__}() fn  ended')

def add_function(**kwargs):
    print("Welcome")
    print(kwargs['no1']+kwargs['no2'])
    return True

if __name__ == '__main__':
    call_function(add_function,no1=1,no2=2)

    call_function(add_function,no1=45,no2=20)