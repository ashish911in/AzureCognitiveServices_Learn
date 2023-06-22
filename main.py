from pytictoc import TicToc

time = TicToc()

def main():
    print("main() function started")
    pass
    print("main() function ended")

if __name__ == "__main__":
   time.tic()
   main()
   time.toc()