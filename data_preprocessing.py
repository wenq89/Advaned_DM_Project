import json
from collections import defaultdict

FILE_LIST = ["date", "everyday", "formal affair", "other", "party", "vacation", "wedding", "work"]

HEIGHT = {
    'FOOT': 30.48,
    'INCH': 2.54,
}

SIZE = {
    8: 81,
    10: 86,
    12: 91.5,
    14: 96.5,
    16: 101.5,
    18: 106.5,
    20: 112,
    22: 117
}


# missing data in any categories? - to decide COSINE OR CENTERED COSINE
def find_purposes():
    # example = [{'rented for': 'party', 'count': 0}]
    purposes_dict = defaultdict(int)
    count = 0

    for line in open('files_purposes/renttherunway_final_data.json', 'r'):
        data = json.loads(line)
        if "rented for" not in data:
            count += 1
        else:
            purposes_dict[data["rented for"]] += 1

        # if "height" not in data:
        #     count_1 += 1

    print("The number of tuples does not have the key-\"rented for\": ", count)
    print("The \"rented for\" dictionary:\n", purposes_dict)


def file_generator():
    for line in open('files_purposes/renttherunway_final_data.json', 'r'):
        data = json.loads(line)
        if "rented for" in data:
            purpose_files(data["rented for"], data)

    print("End of file generation\n")


def purpose_files(rent_type, rent_data):
    json_object = json.dumps(rent_data)

    with open("files_purposes/"+rent_type+".json", "a") as outfile:
        outfile.write(json_object)
        outfile.write("\n")


def cos_sim_file_generator():
    for filename in FILE_LIST:
        for line in open('files_purposes/'+filename+'.json', 'r'):
            data = json.loads(line)
            if "height" not in data:
                data["height"] = 0
            else:
                arr_h = data["height"].split(' ')
                feet_cm = float(arr_h[0].replace('\'', ''))*HEIGHT["FOOT"]
                inch_cm = float(arr_h[1].replace('\"', ''))*HEIGHT["INCH"]
                data["height"] = round(feet_cm+inch_cm,2)

            if "weight" not in data:
                data["weight"] = 0
            else:
                data["weight"] = int(data["weight"].replace('lbs', ''))

            # the reference of size to centimeter is from https://www.belladinotte.com/fitting
            body_size = data["size"]
            if body_size > 22 or body_size < 8:
                data["size"] = 0
            else:
                if body_size % 2 == 0:
                    data["size"] = SIZE[body_size]
                else:
                    data["size"] = SIZE[body_size-1]

            if "age" not in data:
                data["age"] = 0
            else:
                data["age"] = int(data["age"])

            new_data = {
                "height": data["height"],
                "weight": data["weight"],
                "body_size": data["size"],
                "age": data["age"]
            }

            cos_sim_files(filename, new_data)
        print("End of " + filename + " file generation\n")

    print("End of all cos_sim_files generation\n")


def cos_sim_files(rent_type, simple_data):
    json_object = json.dumps(simple_data)

    with open("files_cos_sim/cos_sim_"+rent_type+".json", "a") as outfile:
        outfile.write(json_object)
        outfile.write("\n")


cos_sim_file_generator()
# file_generator()


