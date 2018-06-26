import json
import collections, re
from pprint import pprint

json_data = open("Video_Games_5.json").read()
with open('Video_Games_5.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
summary = 0
j, i = 0, 0
size = 10000
mylist=[]
while j < size:
    if int((json_data)[i]['overall']) == 5:
        mylist.append(str(json_data[i]['reviewText']).lower())
        summary = summary + len(str(json_data[i]['reviewText']).split())
        print(summary)
        j += 1
    i += 1

bagsofwords = [collections.Counter(re.findall(r'\w+', txt))
               for txt in mylist]
sumbags = sum(bagsofwords, collections.Counter())
print(sumbags)
ob = open("5star.txt","w")
ob.write(str(sumbags))