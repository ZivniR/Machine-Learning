import json
import collections, re
import operator
from pprint import pprint

class Bow1:
    def nonecheak(vals):
        if vals is None:
            vals = 0
        return vals


    def compute(self,json_data,stars):
        i, j = 0, 0
        right, wrong, overall = 0, 0, 0
        super1,super2,super3,super4,super5= 0,0,0,0,0

        grades = {'5stars': 0, '4stars': 0, '3stars': 0, '2stars': 0, '1stars': 0}
        words = []
        star5 = []
        star4 = []
        star3 = []
        star2 = []
        star1 = []

        mylist=[]
        k = 0
        #while j < len(json_data):
        ob = open('list.txt', 'r', encoding='utf8')
        while k < 66:
            line = ob.readline()
            lines = list(line.split())
            #print(lines[0])
            words.append(lines[0])
            #print(words)
            lines1 = lines[1:6]
            lines1 = [int(x) for x in lines1]
            lines1.sort()
            #print(lines1)
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
            k += 1

        while j < 1:
            if int((json_data)['overall']) == stars:
                mylist.append(str(json_data['reviewText']).lower())
                j+=1
                #print(j)


                bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
                            for txt in mylist ]

                for obj in bagsofwords:
                    k=0
                    while k< len(words):
                        val = obj.get(words[k])
                        val = Bow1.nonecheak(val)
                        if val > 0:
                            grades['5stars'] += (star5[k] *val)
                            grades['4stars'] += (star4[k] *val)
                            grades['3stars'] += (star3[k] *val)
                            grades['2stars'] += (star2[k] *val)
                            grades['1stars'] += (star1[k] *val)
                        k+=1

                    val1 = obj.get('fail')
                    val1 = Bow1.nonecheak(val1)
                    val2 = obj.get('failed')
                    val2 = Bow1.nonecheak(val2)
                    val =  val1+val2
                    if val > 0:
                        grades['5stars'] += (1 * val)
                        grades['4stars'] += (2 * val)
                        grades['3stars'] += (3 * val)
                        grades['2stars'] += (4 * val)
                        grades['1stars'] += (5 * val)
                #print(grades)

                if grades['5stars'] > grades['4stars'] and grades['5stars'] > grades['3stars'] and grades['5stars'] > grades['2stars'] and grades['5stars'] > grades['1stars']:
                    print("*****")
                    overall = 5
                    return 5
                if grades['4stars'] > grades['5stars'] and grades['4stars'] > grades['3stars'] and grades['4stars'] > grades['2stars'] and grades['4stars'] > grades['1stars']:
                    print("****")
                    overall = 4
                    return 4
                if grades['3stars'] > grades['4stars'] and grades['3stars'] > grades['5stars'] and grades['3stars'] > grades['2stars'] and grades['3stars'] > grades['1stars']:
                    print("***")
                    overall = 3
                    return 3
                if grades['2stars'] > grades['4stars'] and grades['2stars'] > grades['3stars'] and grades['2stars'] > grades['5stars'] and grades['2stars'] > grades['1stars']:
                    print("**")
                    overall = 2
                    return 2
                if grades['1stars'] > grades['4stars'] and grades['1stars'] > grades['3stars'] and grades['1stars'] > grades['2stars'] and grades['5stars'] < grades['1stars']:
                    print("*")
                    overall = 1
                    return 1
                mylist.clear()
                bagsofwords.clear()
                grades={x: 0 for x in grades}
                if overall == int((json_data)[i]['overall']):
                    right+=1

                else:
                    wrong+=1

                if overall == 5:
                    super5+=1
                if overall == 4:
                    super4+=1
                if overall == 3:
                    super3+=1
                if overall == 2:
                    super2+=1
                if overall == 1:
                    super1+=1
            i += 1
        #print("right:"+str(right)+" wrong:"+str(wrong))
        #print("5: "+str(super5)+" 4: "+str(super4)+" 3: "+str(super3)+" 2: "+str(super2)+" 1: "+str(super1))
        return grades