from azure.ai.textanalytics import TextAnalyticsClient
import azure_connect as connector
import environment_variables as ev
from input_output import file_io

def create_text_analytics_client(key,endpoint):
    print(f"create_text_analytics_client({type(key)},{type(endpoint)}) fn started")
    ta_credential = connector.authenticate_client(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    print("create_text_analytics_client() fn ended")
    return text_analytics_client

def language_detection(inputText, text_client):
    print(f"language_detection({type(inputText)},{type(credentials)}) fn has started")
    try:
        response = text_client.detect_language(documents = inputText, country_hint = 'us')
        docs = [doc for doc in response if doc.is_error==False]
        print("Response:",  response[0])
        file_io.file_write_print(response)
        for doc in docs:
            print("Language: ", doc.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
    print(f"language_detection() fn has ended")

def analyze_sentiment(inputText, text_client):
    print(f"analyze_sentiment({type(inputText)},{type(credentials)}) fn has started")
    try:
        response = text_client.analyze_sentiment(inputText,show_opinion_mining=True)[0]
        print(response)
        file_io.file_write_print(response)
    
    except Exception as err:
        print("Encountered exception. {}".format(err))

    print(f"analyze_sentiment() fn has ended")

def recognize_entities(inputText,text_client):
    print("recognize_entities() fn started")
    try:
        response = text_client.recognize_entities(inputText)
        # print(response)
        file_io.file_write_print(response)
        for entity_list in response:
            print(entity_list)
            for entity in entity_list.entities:
                print(entity)

    except Exception as err:
        print("Encountered exception. {}".format(err))
    print("recognize_entities() fn ended")

def analyse_text(inputText):
    print(f"analyse_text({type(inputText)}) fn has started")
    credentials = dict()
    credentials["Key"] = ev.get_env_variable('API_Key')
    credentials["End_Point"] = ev.get_env_variable('End_Point')
    text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
    language_detection(inputText, text_client)
    # analyze_sentiment(inputText,text_client)
    # recognize_entities(inputText,text_client)
    print(f"analyse_text() fn has ended")
    
if __name__ == "__main__":
   from pytictoc import TicToc
   time_tracker = TicToc()
   time_tracker.tic()
   # import environment_variables as ev
   import sys
   credentials = dict()
   credentials["Key"] = ev.get_env_variable('API_Key')
   credentials["End_Point"] = ev.get_env_variable('End_Point')
   # textClient = createTextAnalyticsClient(key,endpoint)
   # print(textClient,type(textClient))
   inputText = [
       """
       This is a paragraph.
       I have never seen something so difficult.
       """,
       """
       2nd sentence. James not happy.
       """
       ]
   
   text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
   language_detection(inputText, text_client)
   # analyze_sentiment(inputText,text_client)
   # recognize_entities(inputText,text_client)
   time_tracker.toc()