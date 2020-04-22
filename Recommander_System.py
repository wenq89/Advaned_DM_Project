import json
from collections import Counter

# with open('renttherunway_final_data.json') as f:
#    data = json.load(f)
#
# # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}

dict = {}
list = []
count = 0
summ = 0
for line in open('files_purposes/renttherunway_final_data.json', 'r'):
   # player = json.loads(line)
   # c = Counter(player["item_id"] for player in json_obj)
   a = json.loads(line)
   list.append(a["item_id"])
   print(len(list))

counter = Counter(list)
print(counter)
#    # print(type(a))
#    # tweets.append(json.loads(line))
#    # print(type(tweets))
#    count += 1
#    # print(type(a["rating"]) == str)
#    if type(a["rating"]) != str:
#       print(a["rating"])
#    else:
#       summ += int(a["rating"])

#
# print(summ/count)
# # print(len(set))

