from dotenv import load_dotenv
load_dotenv()
import os

def test():
    check = os.getenv('API_Key')
    print(check)
    if check:
        print('c:',check)
    else:
        os.environ['API_Key'] = "a13fda58da4245a7955b43ad8fbdd803"
        print("Key set")
        print(os.getenv('API_Key'))

def get_env_variable(variable):
    print(f"Entered get_env_variable({type(variable)}) function")
    return os.getenv(variable)

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
    test()
    time_tracker.toc()