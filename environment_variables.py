from dotenv import load_dotenv
load_dotenv()
import os
import logging

def test():
    check = get_env_variable('API_Key')
    print(check)
    if check:
        print('c:',check)
    else:
        os.environ['API_Key'] = "po"
        print("Key set")
        print(get_env_variable('API_Key'))

def get_env_variable(variable):
    logging.info(f"Entered get_env_variable({variable}) function")
    return os.environ[variable]

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
    test()
    time_tracker.toc()