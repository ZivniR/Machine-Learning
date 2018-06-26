import json
import collections, re
import operator
from pprint import pprint
import math

class Bow4:

    def nonecheak(vals):
        if vals is None:
            vals = 0
        return vals


    def compute(self,json_data,stars):

        i, j = 0, 0
        right, wrong, overall = 0, 0, 0
        super1, super2, super3, super4, super5 = 0, 0, 0, 0, 0


        grades = []
        words = []
        status = []
        grade = 0

        q = 0
        ob = open("list 2.txt",'r')
        while q < 152:
            change=ob.readline()
            changelist=change.split()
            #print(changelist[0])
            words.append(changelist[0])
            status.append(int(changelist[1]))
            q +=1

        #print(len(status))
        #print(len(words))

        mylist = []
# while j < len(json_data):
        while j < 1:
            if int((json_data)['overall']) == stars:
                mylist.append(str(json_data['reviewText']).lower())
                j += 1
                #print(j)

                bagsofwords = [collections.Counter(re.findall(r'\w+', txt))
                            for txt in mylist]
        # print("1")
        # sumbags = sum(bagsofwords, collections.Counter())

        # print(sumbags)
#               print("go")

                for obj in bagsofwords:
                    k = 0
                    while k < len(words):
                        val = obj.get(words[k])
                        val = Bow4.nonecheak(val)
                        if val > 0:
                            grade += (status[k] * val)
                        k += 1


                grades.append(grade)
                #print(grade)

                if grade >= 3:
                    print("*****")
                    overall = 5
                    return 5
                if grade >= 2 and grade < 3:
                    print("****")
                    overall = 4
                    return 4
                if grade >= 1 and grade < 2:
                    print("***")
                    overall = 3
                    return 3
                if grade >= 0 and grade < 1:
                    print("**")
                    overall = 2
                    return 2
                if grade < 0:
                    print("*")
                    overall = 1
                    return 1
                mylist.clear()
                bagsofwords.clear()
                grade = 0
                if overall == int((json_data)[i]['overall']):
                    right += 1

                else:
                    wrong += 1

                if overall == 5:
                    super5 += 1
                if overall == 4:
                    super4 += 1
                if overall == 3:
                    super3 += 1
                if overall == 2:
                    super2 += 1
                if overall == 1:
                    super1 += 1

            i += 1

        if stars == 5:
            super5 += super4
        if stars == 4:
            super4 += super3
            super4 += super5
        if stars == 3:
            super3 += super4
            super3 += super2
        if stars == 2:
            super2 += super3
            super2 += super1
        if stars == 1:
            super1 += super2

        avr=0
        #print("right:" + str(right) + " wrong:" + str(wrong))
        #print("5: " + str(super5) + " 4: " + str(super4) + " 3: " + str(super3) + " 2: " + str(super2) + " 1: " + str(super1))
        for index in grades:
            avr=avr+index
        avr=avr/len(grades)
        print(avr)
        return {"five_stars": super5 , "four_stars": super4 , "three_stars": super3 , "two_stars": super2 , "one_star ": super1}