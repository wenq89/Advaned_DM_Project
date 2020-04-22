import math
import json
# implementation of centered cosine similarity
user_data = {
                "height": 160.02,
                "weight": 112,
                "body_size": 81,
                "age": 27
            }

TOP_CANDIDATES = []
#
# {'height': 172.72, 'weight': 138, 'body_size': 81, 'age': 45}
# 0.9655996465615181
# {'height': 160.02, 'weight': 0, 'body_size': 81, 'age': 29}
# 0.597335448954644
# {'height': 167.64, 'weight': 110, 'body_size': 0, 'age': 24}
# 0.9547050359782222
# {'height': 165.1, 'weight': 135, 'body_size': 96.5, 'age': 29}
# 0.9811834443022317
# {'height': 154.94, 'weight': 112, 'body_size': 0, 'age': 32}
# 0.930290752083521
# {'height': 147.32, 'weight': 155, 'body_size': 112, 'age': 23}
# 0.6854633466448226
# {'height': 170.18, 'weight': 165, 'body_size': 101.5, 'age': 31}
# 0.8367119606988891
# {'height': 162.56, 'weight': 106, 'body_size': 0, 'age': 36}
# 0.9560607845798733

def run_algo(user_info):
    # print(user_info)
    # user_info = subtract_average(user_info)
    # print(user_info)
    for line in open('files_cos_sim/cos_sim_date.json', 'r'):
        curr_info = json.loads(line)
        # print(curr_info)
        # curr_info = subtract_average(curr_info)
        # print(curr_info)
        result = cos_sim_algo(curr_info, user_info)
        print(result)

# cos(d1, d2) = d1*d2/sqrt(d1^2)*sqrt(d2^2)
def cos_sim_algo(data1, data2):
    numerator = data1["height"]*data2["height"] + data1["weight"]*data2["weight"] + data1["body_size"]*data2["body_size"]
    d1 = math.sqrt(data1["height"]*data1["height"] + data1["weight"]*data1["weight"] + data1["body_size"]*data1["body_size"])
    d2 = math.sqrt(data2["height"]*data2["height"] + data2["weight"]*data2["weight"] + data2["body_size"]*data2["body_size"])
    return numerator/d1*d2


def subtract_average(person_info):
    average = round((person_info["height"]+person_info["weight"]+person_info["body_size"])/3, 2)
    if person_info["height"] != 0:
        person_info["height"] -= average
    if person_info["weight"] != 0:
        person_info["weight"] -= average
    if person_info["body_size"] != 0:
        person_info["body_size"] -= average
    return person_info

run_algo(user_data)