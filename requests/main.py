import json.decoder

import requests

if __name__ == "__main__":
    # response = requests.get('http://jsonplaceholder.typicode.com/todos')
    response = requests.get('http://jsonplaceholder.typicode.com/users', params="id=5&id=7")
    print(response.status_code)

    try:
        # json_file = response.json()
        json_f = json.loads(response.text)
        print(json_f)



    except json.decoder.JSONDecodeError:
        print('json decode error')
    else:
        print('json loaded')
