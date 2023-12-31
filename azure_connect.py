from azure.core.credentials import AzureKeyCredential
import logging

# Authenticate the client using your key and return a credential 
def authenticate_client(key):
    logging.info(f"authenticate_client({type(key)}) fn started")
    ta_credential = AzureKeyCredential(key)
    logging.info("authenticate_client() fn ended")
    return ta_credential

if __name__ == "__main__":
   from pytictoc import TicToc
   time_tracker = TicToc()
   time_tracker.tic()
   import environment_variables as ev
   key = ev.get_env_variable('API_Key')
   to_print = authenticate_client(key)
   print(to_print,type(to_print))
   time_tracker.toc()