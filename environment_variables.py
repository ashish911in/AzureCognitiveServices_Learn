import os

def test():
    for k, v in os.environ.items():
        print(f'{k}={v}')
    check = os.getenv('API_Key')
    print(check)
    if check:
        print(check)
    else:
        os.environ['API_Key'] = "a13fda58da4245a7955b43ad8fbdd803"
        print("Key set")
        print(os.getenv('API_Key'))

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
    test()
    time_tracker.toc()