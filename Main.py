from GUI import GUI
from Bow4 import Bow4
from Bow1 import Bow1
import json

#json_data = open("Video_Games_5.json").read()
#with open('Sports_and_Outdoors_5.json', 'r') as handle:
#    json_data = [json.loads(line) for line in handle]

with open('Video_Games_5.json', 'r') as handle:
    json_data = [json.loads(line) for line in handle]
j, i = 0, 50000

gui = GUI()
bow = Bow4()
bow1 = Bow1()
bright, bworng = 0, 0
gright, gworng = 0, 0
agree = 0
disagree = 0

stars = 4

while j < 10000:
    if int((json_data)[i]['overall']) == stars:
        #print((json_data)[i]['reviewText'])
        gres = gui.compute(json_data[i],stars)
        bres = bow.compute(json_data[i],stars)
        if bres == gres:
            print("the grade should be:" +str(bres))
        else:
            print("bow4= " + str(bres) +" GUI= " + str(gres) + " overall= " + str((json_data)[i]['overall']))
        j += 1
        if stars == bres or bres == stars-1 or bres == stars+1:
            bright += 1
        else:
            bworng += 1
        if stars == gres or gres == stars-1 or gres == stars+1:
            gright += 1
        else:
            gworng += 1
        if bres == stars or stars == gres or gres == stars-1 or bres == stars-1 or bres == stars+1 or gres == stars+1:
            agree += 1
        else:
            disagree += 1
    i += 1

print ("bres: right= " + str(bright) + " wrong= " + str(bworng) )
print ("gres: right= " + str(gright) + " wrong= " + str(gworng) )
print ("agree= " + str(agree) + " disagree= " + str(disagree) )