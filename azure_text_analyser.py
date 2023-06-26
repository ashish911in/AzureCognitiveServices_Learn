from azure.ai.textanalytics import TextAnalyticsClient
import azure_connect as connector
import environment_variables as ev
from input_output import file_io
import logging
import sys
from helpers import converters
logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)

def create_text_analytics_client(key,endpoint):
    '''
    create the text analytics client object with the given key and end point

            Parameters:
                    key (str): API key
                    endpoint (str): API end point URL

            Returns:
                    text_analytics_client (TextAnalyticsClient): an object to perform text analytics API calls
    '''
    logging.info(f"create_text_analytics_client({type(key)},{type(endpoint)}) fn started")
    ta_credential = connector.authenticate_client(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    logging.info("create_text_analytics_client() fn ended")
    return text_analytics_client

def language_detection(input_text, text_client):
    '''
    Detect the main language using Azure Cognitive Services

            Parameters:
                    input_text (list): The text to be analysed
                    text_client (TextAnalyticsClient): The object to perform text analytics API calls

            Returns:
                    Does not return anything
    '''
    logging.info(f"language_detection({type(input_text)},{type(text_client)}) fn has started")
    response = ''
    response_dict = {
            'input': input_text,
            'data': []
        }
    try:
        response = text_client.detect_language(documents = input_text, country_hint = 'us')
        results = [result for result in response if result.is_error==False]
        for text in results:
            temp_dict1 = dict()
            temp_dict1['id'] = text['id']
            temp_dict1['primary_language'] = {
                'name': text.primary_language.name,
                'confidence_score': text.primary_language.confidence_score
            }
            response_dict['data'].append(temp_dict1)

    except Exception as err:
        print("Encountered exception. {}".format(err))
    
    file_io.file_write_print(response)
    file_io.json_write(response_dict)
    logging.info(f"language_detection() fn has ended")
    return converters.dict_to_json(response_dict)

def analyze_sentiment(input_text, text_client):
    '''
    Analyse the sentiment of the text using Azure Cognitive Services

            Parameters:
                    input_text (list): The text to be analysed
                    text_client (TextAnalyticsClient): The object to perform text analytics API calls

            Returns:
                    Does not return anything
    '''
    logging.info(f"analyze_sentiment({type(input_text)},{type(text_client)}) fn has started")
    response = ''
    response_dict = {
            'input': input_text,
            'data': []
        }
    try:
        response = text_client.analyze_sentiment(input_text,show_opinion_mining=False)
        results = [result for result in response if not result['is_error']]
        for text in results:
            temp_dict1 = dict()
            temp_dict1['id'] = text['id']
            temp_dict1['sentiment'] = text['sentiment']
            temp_dict1['data'] = []
            for sentence in text['sentences']:
                temp_dict2 = dict()
                temp_dict2['text'] = sentence['text']
                temp_dict2['sentiment'] = sentence['sentiment']
                temp_dict2['length'] = sentence['length']
                temp_dict2['offset'] = sentence['offset']
                temp_dict2['confidence_score'] = {
                    'positive':sentence['confidence_scores'].positive,
                    'neutral':sentence.confidence_scores.neutral,
                    'negative':sentence['confidence_scores'].negative
                }
                temp_dict1['data'].append(temp_dict2)
            response_dict['data'].append(temp_dict1)


    except Exception as err:
        print("Encountered exception. {}".format(err))
        type_check, value, traceback = sys.exc_info()
        print(type_check)
        print(value)
        print(traceback)
    
    file_io.file_write_print(response)
    file_io.json_write(response_dict)
    logging.info(f"analyze_sentiment() fn has ended")
    return converters.dict_to_json(response_dict)

def recognize_entities(input_text,text_client):
    '''
    Recognize the entities present in the text using Azure Cognitive Services

            Parameters:
                    input_text (list): The text to be analysed
                    text_client (TextAnalyticsClient): The object to perform text analytics API calls

            Returns:
                    Does not return anything
    '''
    logging.info("recognize_entities() fn started")
    response = ''
    response_dict = {
        'input': input_text,
        'data': []
    }
    temp_dict1, temp_dict2 = {},{}
    # temp_list = []
    try:
        response = text_client.recognize_entities(input_text)
        # print(response)
        for entity_list in response:
            temp_dict1 = dict()
            temp_dict1['id'] = entity_list['id']
            temp_dict1['data'] = []
            for entity in entity_list.entities:
                temp_dict2 = dict()
                temp_dict2['text'] = entity.text
                temp_dict2['category'] = entity.category
                temp_dict2['subcategory'] = entity.subcategory
                temp_dict2['length'] = entity.length
                temp_dict2['offset'] = entity.offset
                temp_dict2['confidence_score'] = entity.confidence_score
                temp_dict1['data'].append(temp_dict2)
            response_dict['data'].append(temp_dict1)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        type_check, value, traceback = sys.exc_info()
        print(type_check)
        print(value)
        print(traceback)

    file_io.file_write_print(response)
    file_io.json_write(response_dict)
    logging.info("recognize_entities() fn ended")
    return converters.dict_to_json(response_dict)
    
"""
def dynamic_classify_doc_label(input_document, text_client):
    '''
    Function to classify a document

            Parameters:
                    input_document (list): The text to be analysed
                    text_client (TextAnalyticsClient): The object to perform text analytics API calls

            Returns:
                    Does not return anything
    '''
    logging.info(f"dynamic_classify_doc_label() fn has started")
    response = ''
    try:
        response = text_client.dynamic_classification(input_document)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        type_check, value, traceback = sys.exc_info()
        print(type_check)
        print(value)
        print(traceback)

    file_io.file_write_print(response)
    logging.info(f"dynamic_classify_doc_label() fn has ended")
"""

def analyse_text(input_text):
    '''
    Main analyse function from which other functions are called

            Parameters:
                    input_text (list): The text to be analysed

            Returns:
                    Does not return anything
    '''
    logging.info(f"analyse_text({type(input_text)}) fn has started")
    credentials = dict()
    credentials["Key"] = ev.get_env_variable('API_Key')
    credentials["End_Point"] = ev.get_env_variable('End_Point')
    text_client = create_text_analytics_client(credentials['Key'],credentials['End_Point'])
    choice = 0

    functions_dict = {
        '1' : language_detection,
        '2' : analyze_sentiment,
        '3' : recognize_entities#,
        # '4': dynamic_classify_doc_label
    }
    exit_choice = '5'
    while(choice!=exit_choice):
        print('1. Language Detection')
        print('2. Sentiment Analysis')
        print('3. Entities Detection')
        print('4. Single Label Classify (inactive)')
        print('5. Exit')
        choice = input('Enter a choice:')
        if choice in functions_dict.keys():
            print(functions_dict[choice](input_text,text_client))
        elif choice==exit_choice:
            break
        else:
            print('Invalid option. Try again !! \n')
    logging.info(f"analyse_text() fn has ended")
    
if __name__ == "__main__":
   from pytictoc import TicToc
   time_tracker = TicToc()
   time_tracker.tic()
   input_text = [
       """
       This is a paragraph.
       I have never seen something so difficult. 2nd sentence. James not happy.
       Microsoft is not there in London, UK.
       """,
       """
       2nd sentence. James not happy.
       """
       ]
   analyse_text(input_text)
   time_tracker.toc()