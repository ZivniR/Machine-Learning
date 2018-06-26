import re
ob = open('C:/Users/Ziv-Nir/Desktop/ml1.txt','r',encoding='utf8')
i, j = 0, 1
words = []
star5,star4,star3,star2,star1=[],[],[],[],[]

while i < 2:
    line = ob.readline()
    i += 1

while line != EOFError:
    line = ob.readline()
    lines = list(line.split())
    print(lines[0])
    words.append(lines[0])
    print(words)
    lines1=lines[1:6]
    lines1=[int(x) for x in lines1]
    lines1.sort()
    print(lines1)
    if int(lines[1]) == lines1[4]:
        star5.append(5)
    if int(lines[1]) == lines1[3]:
        star5.append(4)
    if int(lines[1]) == lines1[2]:
        star5.append(3)
    if int(lines[1]) == lines1[1]:
        star5.append(2)
    if int(lines[1]) == lines1[0]:
        star5.append(1)
    if int(lines[2]) == lines1[4]:
        star4.append(5)
    if int(lines[2]) == lines1[3]:
        star4.append(4)
    if int(lines[2]) == lines1[2]:
        star4.append(3)
    if int(lines[2]) == lines1[1]:
        star4.append(2)
    if int(lines[2]) == lines1[0]:
        star4.append(1)
    if int(lines[3]) == lines1[4]:
        star3.append(5)
    if int(lines[3]) == lines1[3]:
        star3.append(4)
    if int(lines[3]) == lines1[2]:
        star3.append(3)
    if int(lines[3]) == lines1[1]:
        star3.append(2)
    if int(lines[3]) == lines1[0]:
        star3.append(1)
    if int(lines[4]) == lines1[4]:
        star2.append(5)
    if int(lines[4]) == lines1[3]:
        star2.append(4)
    if int(lines[4]) == lines1[2]:
        star2.append(3)
    if int(lines[4]) == lines1[1]:
        star2.append(2)
    if int(lines[4]) == lines1[0]:
        star2.append(1)
    if int(lines[5]) == lines1[4]:
        star1.append(5)
    if int(lines[5]) == lines1[3]:
        star1.append(4)
    if int(lines[5]) == lines1[2]:
        star1.append(3)
    if int(lines[5]) == lines1[1]:
        star1.append(2)
    if int(lines[5]) == lines1[0]:
        star1.append(1)
    print(star1)
    print(star2)
    print(star3)
    print(star4)
    print(star5)
    print(len(star1))
    print(len(star2))
    print(len(star3))
    print(len(star4))
    print(len(star5))
    print(len(words))