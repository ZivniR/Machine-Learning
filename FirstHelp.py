import re
ob = open('list.txt','r',encoding='utf8')
i=0
words = []
star5,star4,star3,star2,star1 = [],[],[],[],[]
j = 0



while i < 66:
    line = ob.readline()
    lines = list(line.split())
    print(lines[0])
    words.append(lines[0])
    print(words)
    star5.append(float(lines[1]) / (float(lines[6])*181.5982))
    print(star5)
    star4.append(float(lines[2]) / (float(lines[6])*231.3604))
    print(star4)
    star3.append(float(lines[3]) / (float(lines[6])*252.6672))
    print(star3)
    star2.append(float(lines[4]) / (float(lines[6])*242.6207))
    print(star2)
    star1.append(float(lines[5]) / (float(lines[6])*173.5541))
    print(star1)
    i += 1
print(words)
