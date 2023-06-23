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

def language_detection(inputText, credentials):
    print(f"language_detection({type(inputText)},{type(credentials)}) fn has started")
    try:
        text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
        response = text_client.detect_language(documents = inputText, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)
        print("Response:",  response)

    except Exception as err:
        print("Encountered exception. {}".format(err))
    print(f"language_detection() fn has started")

def analyze_sentiment(inputText, credentials):
    print(f"analyze_sentiment({type(inputText)},{type(credentials)}) fn has started")
    try:
        text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
        response = text_client.analyze_sentiment(inputText,show_opinion_mining=True)[0]
        print(response)
        file_io.file_write(response)
    
    except Exception as err:
        print("Encountered exception. {}".format(err))

    print(f"analyze_sentiment() fn has started")

def analyse_text(inputText):
    print(f"analyse_text({type(inputText)}) fn has started")
    credentials = dict()
    credentials["Key"] = ev.get_env_variable('API_Key')
    credentials["End_Point"] = ev.get_env_variable('End_Point')
    # language_detection(inputText, credentials)
    analyze_sentiment(inputText,credentials)
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
       """
       ]
   language_detection(inputText, credentials)
   time_tracker.toc()