import json
import collections, re
from pprint import pprint

while 1:
json_data = open("Video_Games_5.json").read()
with open('Video_Games_5.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
j, i, k= 0, 0, 1
size=10000
mylist=[]
summary = 0
sum1=0
ob=open('bagsofwords.txt','w')
while k < 6:
    while j < size:
            if int((json_data)[i]['overall']) == k:
                mylist.append(str(json_data[i]['reviewText']).lower())
                summary = summary + len(str(json_data[i]['reviewText']).split())
                print(summary)
                j+=1
            i+=1

    bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
                for txt in mylist ]
    sumbags = sum(bagsofwords, collections.Counter())
    summary=summary/size
    print("summary= " + str(summary))
    print(sumbags.most_common(300))
    ob.write(str(k)+" stars:\n")
    ob.write(str(sumbags.most_common(300))+'\n')
    ob.write("average amount of words:"+str(summary)+'\n')
    k+=1
    sumbags.clear()
    bagsofwords.clear()
    i, j = 0, 0
    summary = 0
ob.close()