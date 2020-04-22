import math
import json
from person_info import *
# TESTING DATA
# {"user_id": "136279", "item_id": "330238", "height": 167.64, "weight": 115, "body_size": 4, "age": 32}
user_data = {
                "height": 167.64,
                "weight": 115,
                "body_size": 4,
                "age": 32
            }

TOP_CANDIDATES = []
NUM_TOP_CANDIDATES = 20

def run_algo(user_info):
    min_cos_sim_val = 0
    user_normalized_info = subtract_average(info_normalization(user_info))

    for line in open('files_cos_sim/cos_sim_date.json', 'r'):
        curr_info = json.loads(line)
        curr_normalized_info = subtract_average(info_normalization(curr_info))
        cos_sim_val = cos_sim_algo(curr_normalized_info, user_normalized_info)
        if len(TOP_CANDIDATES) <= NUM_TOP_CANDIDATES and cos_sim_val > min_cos_sim_val:
            curr_info["cos_sim_val"] = cos_sim_val
            TOP_CANDIDATES.append(curr_info)
       # print(cos_sim_val)
    print(*sorted(TOP_CANDIDATES, key = lambda i: i["cos_sim_val"], reverse = True), sep="\n")
    # print(TOP_CANDIDATES)
    # will weight age as a criteria to regenerate the top candidates.

# cos(d1, d2) = d1*d2/sqrt(d1^2)*sqrt(d2^2)
def cos_sim_algo(data1, data2):
    numerator = data1["height"]*data2["height"] + data1["weight"]*data2["weight"] + data1["body_size"]*data2["body_size"]
    d1 = math.sqrt(data1["height"]*data1["height"] + data1["weight"]*data1["weight"] + data1["body_size"]*data1["body_size"])
    d2 = math.sqrt(data2["height"]*data2["height"] + data2["weight"]*data2["weight"] + data2["body_size"]*data2["body_size"])
    if d1 == 0 or d2 == 0:
        return 0
    else:
        return round(numerator/d1*d2,2)


def subtract_average(person_info):
    average = round((person_info["height"]+person_info["weight"]+person_info["body_size"])/3, 2)
    # print(average)
    if person_info["height"] != 0:
        person_info["height"] -= average
    if person_info["weight"] != 0:
        person_info["weight"] -= average
    if person_info["body_size"] != 0:
        person_info["body_size"] -= average
    return person_info

run_algo(user_data)