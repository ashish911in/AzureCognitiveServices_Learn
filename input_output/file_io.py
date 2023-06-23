import json
# all file input 1st

# all file ouput 2nd

def json_write(data):
    print('start')
    
    with open('.\input_output\output.json', 'w') as outfile:
        json.dump(data, outfile)

    print('end')

def file_write(data):
    print('start')
    with open('.\input_output\output_file.txt', 'w') as outfile:
        outfile.write(data)
    print('end')

if __name__ == '__main__':
    from pytictoc import TicToc
    time_tracker = TicToc()
    time_tracker.tic()
    json_data = {
        "l": [
            {
                "k": 23
            }
        ]
    }
    text_data = [
        """
        This is a sample data.
        Please dont judge
        """
    ]
    json_write(json_data)

    time_tracker.toc()