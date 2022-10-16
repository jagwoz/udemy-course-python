import json.decoder

import requests

if __name__ == "__main__":
    response = requests.get('http://videokurs.pl')
    print(response.status_code)

    try:
        json_file = response.json()
    except json.decoder.JSONDecodeError:
        print('json decode error')
    else:
        print('json loaded')
