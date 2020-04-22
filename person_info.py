# personal information normalization
import copy

def info_normalization(user_info):
    user_normalized_info = copy.deepcopy(user_info)
    user_normalized_info["height"] = get_height(user_info["height"])
    user_normalized_info["weight"] = get_weight(user_info["weight"])
    user_normalized_info["body_size"] = get_size(user_info["body_size"])
    return user_normalized_info

def get_height(h):
    if h <= 140:
        return 0
    elif 140 < h <= 150:
        return 1
    elif 150 < h <= 155:
        return 2
    elif 155 < h <= 160:
        return 3
    elif 160 < h <= 165:
        return 4
    elif 165 < h <= 170:
        return 5
    elif 170 < h <= 175:
        return 6
    elif 175 < h <= 180:
        return 7
    elif 180 < h <= 185:
        return 8
    elif 185 < h <= 190:
        return 9
    elif h > 190:
        return 10


def get_weight(w):
    if w <= 90:
        return 0
    elif 90 < w <= 100:
        return 1
    elif 100 < w <= 110:
        return 2
    elif 110 < w <= 120:
        return 3
    elif 120 < w <= 130:
        return 4
    elif 130 < w <= 140:
        return 5
    elif 140 < w <= 150:
        return 6
    elif 150 < w <= 160:
        return 7
    elif 160 < w <= 170:
        return 8
    elif 170 < w <= 180:
        return 9
    elif w > 180:
        return 10


def get_size(s):
    if s < 8:
        return 0
    elif 8 <= s < 10:
        return 1
    elif 10 <= s < 12:
        return 2
    elif 12 <= s < 14:
        return 3
    elif 14 <= s < 16:
        return 4
    elif 16 <= s < 18:
        return 5
    elif 18 <= s < 20:
        return 6
    elif 20 <= s < 22:
        return 7
    elif 22 <= s < 24:
        return 8
    elif 24 <= s < 26:
        return 9
    elif s >= 26:
        return 10
