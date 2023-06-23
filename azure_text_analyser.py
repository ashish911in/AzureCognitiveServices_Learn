from azure.ai.textanalytics import TextAnalyticsClient
import azure_connect as connector
import environment_variables as ev

def create_text_analytics_client(key,endpoint):
    print("create_text_analytics_client() fn started")
    ta_credential = connector.authenticate_client(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    print("create_text_analytics_client() fn ended")
    return text_analytics_client

def language_detection(inputText, credentials):
    try:
        text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
        response = text_client.detect_language(documents = inputText, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)
        print("Response:",  response)

    except Exception as err:
        print("Encountered exception. {}".format(err))

def analyse_text(inputText):
    credentials = dict()
    credentials["Key"] = ev.get_env_variable('API_Key')
    credentials["End_Point"] = ev.get_env_variable('End_Point')
    language_detection(inputText, credentials)


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
   inputText = [sys.argv[1]]
   language_detection(inputText, credentials)
   time_tracker.toc()