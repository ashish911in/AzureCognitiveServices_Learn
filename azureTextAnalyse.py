from azure.ai.textanalytics import TextAnalyticsClient
import azureConnect as conn
import config

def createTextAnalyticsClient(key,endpoint):
    print("createTextAnalyticsClient() fn started")
    ta_credential = conn.authenticate_client(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    print("createTextAnalyticsClient() fn ended")
    return text_analytics_client

def languageDetection(inputText, credentials):
    try:
        textClient = createTextAnalyticsClient(credentials['Key'],credentials['End_Point'])
        response = textClient.detect_language(documents = inputText, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)
        print("Response:",  response)

    except Exception as err:
        print("Encountered exception. {}".format(err))

def analyseText(inputText):
    credentials = dict()
    credentials["Key"] = config.API['Key']
    credentials["End_Point"] = config.API['End_Point']
    languageDetection(inputText, credentials)


if __name__ == "__main__":
   from pytictoc import TicToc
   time = TicToc()
   time.tic()
   credentials = dict()
   credentials["Key"] = config.API['Key']
   credentials["End_Point"] = config.API['End_Point']
   # textClient = createTextAnalyticsClient(key,endpoint)
   # print(textClient,type(textClient))
   inputText = ["Hello how are you?"]
   languageDetection(inputText, credentials)
   time.toc()