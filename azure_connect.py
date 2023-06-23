from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client(key):
    print("authenticate_client() fn started")
    ta_credential = AzureKeyCredential(key)
    print("authenticate_client() fn ended")
    return ta_credential

if __name__ == "__main__":
   from pytictoc import TicToc
   time_tracker = TicToc()
   time_tracker.tic()
   import config
   key = config.API['Key']
   to_print = authenticate_client(key)
   print(to_print,type(to_print))
   time_tracker.toc()