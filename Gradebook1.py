#
#Bryce Benson
#COMP 163
# 12/2/21
# Gradebook Part 1
#

class List():
    def __init__(self, list = []):
        self.list = list
    def average(list):
    # This function calculates the average of a list
        list2 = []
        for i in list:
        # This turns string values of lists into floats
            list2.append(float(i))
        list = list2
        avg = sum(list)/len(list)
        return avg
