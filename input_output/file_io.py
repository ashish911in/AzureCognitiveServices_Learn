import json
import pprint
import os
# all file input 1st

def file_read(file_name):
    try:
        with open('.\\input_output\\'+str(file_name), 'r') as reader:
            print(reader.readlines())
    except Exception as err:
        print("Encountered exception. {}".format(err))

# all file ouput 2nd

def json_write(data):
    print('start')
    
    with open('.\input_output\output.json', 'w') as outfile:
        json.dump(data, outfile)

    print('end')

def file_write_print(data):
    print('file_write_print() start')
    with open('.\input_output\output_file.txt', 'w') as outfile:
        print(data, file=outfile)
    print('file_write_print() end')

def pprint_dict(data):
    pprint.PrettyPrinter(width=7).pprint(data)

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
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
    # file_write_print(json_data)
    file_read('input_file.txt')

    time_tracker.toc()