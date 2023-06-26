import json
import pprint
import sys
# all file input 1st

def file_read(file_name):
    try:
        with open('.\\input_output\\'+str(file_name), 'r') as reader:
            print(reader.readlines())
    except Exception as err:
        print("Encountered exception. {}".format(err))

# all file ouput 2nd

'''
Temporarly placed here
'''
def dict_to_json(data):
    return json.dumps(data)

def json_to_dict(data):
    return json.loads(data)

# End of converters

def json_write(data):
    print(f'json_write({type(data)}) fn has started')
    try:
        with open('.\\input_output\\output.json', 'w') as outfile:
            json.dump(data, outfile)
    except:
        type_check, value, traceback = sys.exc_info()
        print(type_check)
        print(value)
        print(traceback)

    print('json_write() fn has started')
    file_write_print

def file_write_print(data,append=False):
    '''
    Writes the output of print command into a file instead of console with appending possible.

            Parameters:
                    data (any): Any data
                    append (bool): True means append else do not append

            Returns:
                    Does not return anything
    '''
    print('file_write_print() start')
    with open('.\\input_output\\output_file.txt', 'a' if append else 'w') as outfile:
        print(data, file=outfile)
    print('file_write_print() end')

def pprint_dict(data):
    pprint.PrettyPrinter(width=7).pprint(data)

def json_read(file_name):
    logging.info("json_read() fn started")
    with open(file_name,'r') as infile:
        data = json.load(infile)
        logging.info("json_read() fn ending now")
        return data

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
    import logging
    logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
    json_data = {
        "lertter": [
            {
                "ketetet": 23343
            }
        ]
    }
    text_data = [
        """
        This is a sample data.
        Please dont judge
        """
    ]
    # json_write(json_data)
    # pprint_dict(json_data)
    # file_write_print(json_data,True)
    # file_read('input_file.txt')
    p = json_read('.\\input_output\\output.json')
    print(p, type(p))

    time_tracker.toc()