import json
from collections import defaultdict


# missing data in any categories? - to decide COSINE OR CENTERED COSINE
def find_purposes():
    # example = [{'rented for': 'party', 'count': 0}]
    purposes_dict = defaultdict(int)
    count = 0
    for line in open('files/renttherunway_final_data.json', 'r'):
        data = json.loads(line)
        if "rented for" not in data:
            count += 1
        else:
            purposes_dict[data["rented for"]] += 1

    print("The number of tuples does not have the key-\"rented for\": ", count)
    print("The \"rented for\" dictionary:\n", purposes_dict)


def file_generator():
    for line in open('files/renttherunway_final_data.json', 'r'):
        data = json.loads(line)
        if "rented for" in data:
            purpose_files(data["rented for"], data)

    print("End of file generation\n")


def purpose_files(rent_type, rent_data):
    json_object = json.dumps(rent_data)

    with open("files/"+rent_type+".json", "a") as outfile:
        outfile.write(json_object)
        outfile.write("\n")

# find_purposes()
# file_generator()
