import json

def dict_to_json(data):
    return json.dumps(data)

def json_to_dict(data):
    return json.loads(data)

if __name__ == '__main__':
    with open('.\\input_output\\output.json','r') as infile:
        data = json.load(infile)
        p = dict_to_json(data)
        print(p, type(p))