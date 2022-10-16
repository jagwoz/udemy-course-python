import json
import pprint

if __name__ == "__main__":
    json_file = {'name': 'Jacob', 'age': 24, 'kox': True}
    # ensure_ascii - False - pl chars
    # indent - tabs
    json_to_string = json.dumps(json_file, ensure_ascii=False, indent=4, sort_keys=True)
    print(json_to_string)

    with open('json_file.json', 'w', encoding='UTF-8') as file:
        json.dump(json_file, file, ensure_ascii=False, indent=4, sort_keys=True)

    json_file = json.loads(json_to_string)
    print(json_file)

    with open('json_file.json', encoding='UTF-8') as file:
        json_file = json.load(file)
        print(type(json_file))

    pprint.pprint(json_file)
