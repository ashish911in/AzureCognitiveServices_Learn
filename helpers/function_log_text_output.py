def call_function(function_name,args):
    print(f'{function_name.__name__}({type(args[0])},{type(args[1])}) fn started')
    function_name(args[0],args[1])
    print(f'{function_name.__name__}() fn  ended')

def sample_function(arg1, arg2):
    print("Welcome")
    print(arg1+arg2)
    return True

if __name__ == '__main__':
    call_function(sample_function,[1,2])