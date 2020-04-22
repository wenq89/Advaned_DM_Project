import math
import json
from person_info import *
# TESTING DATA
user_data = {
                "height": 175,
                "weight": 130,
                "body_size": 8,
                "age": 27
            }

TOP_CANDIDATES = []

def run_algo(user_info):
    user_info = subtract_average(info_normalization(user_info))

    for line in open('files_cos_sim/cos_sim_date.json', 'r'):
        curr_info = json.loads(line)
        curr_info = subtract_average(info_normalization(curr_info))
        result = cos_sim_algo(curr_info, user_info)
        print(result)

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