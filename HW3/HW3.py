# Eli Jones and William Grantham
# 09/22/2016
# HW3 Q1 Starter Code
# Implementation of interval partitioning algorithm
import datetime
from heapq import heappush , heappop


def scheduleRooms(rooms,cls):
    """
    Input: rooms - list of available rooms
           cls   - dictionary mapping class names to pair of (start,end) times
    Output: Return a dictionary mapping the room name to a list of
    non-conflicting scheduled classes.
    If there are not enough rooms to hold the classes, return 'Not enough rooms'.
    """
    rmassign = {}
    PQ = []
    for i in cls:
        x = cls[i] #grab dictionary tuple
        y = x[0]   #first value
        z = x[1]   #second value
        if y < z:  #compare to get start time
            heappush(PQ, (y, cls[i], i))
        else:
            heappush(PQ, (z, cls[i], i))
    counter = 0
    while PQ:
        temp = heappop(PQ)
        start = temp[0]
        key = temp[1]  #not actually key. its the value in the key
        name = (temp[2]) #this is the real key
        namtup = (name,)
        key = namtup + key
        for j in rooms:
            if j in rmassign:
                assigned = list(rmassign.get(j))
                lengths = len(assigned)
                assend = assigned[lengths-1]
                if assend <= start:
                    del assigned[lengths-1]
                    del assigned[lengths -2]
                    assigned = tuple(assigned)
                    rmassign[j] = assigned + (key) #adds class and times
                    counter += 1
                    break
            elif not (rmassign.has_key(j)): #if the room doesn't have anything store
                rmassign[j] = (key)
                counter += 1
                break

    #deletes last two remaining times in rmassign
    for k in rmassign:
        dell = list(rmassign[k])
        length = len(dell)
        del dell[length-1]
        del dell[length-2]
        dell = tuple(dell)
        rmassign[k] = dell

    if counter < len(cls):
        return "There are not enough rooms!"
    return rmassign

if __name__=="__main__":
    cl1 = {"a": (datetime.time(9),datetime.time(10,30)),
           "b": (datetime.time(9),datetime.time(12,30)),
           "c": (datetime.time(9),datetime.time(10,30)),
           "d": (datetime.time(11),datetime.time(12,30)),
           "e": (datetime.time(11),datetime.time(14)),
           "f": (datetime.time(13),datetime.time(14,30)),
           "g": (datetime.time(13),datetime.time(14,30)),
           "h": (datetime.time(14),datetime.time(16,30)),
           "i": (datetime.time(15),datetime.time(16,30)),
           "j": (datetime.time(15),datetime.time(16,30))}
    rm1 = [1,2,3]
    print cl1
    print scheduleRooms(rm1,cl1)
    print scheduleRooms([1,2],cl1)
    ensrooms = ['KEH U1','KEH M1','KEH M2','KEH M3','KEH U2','KEH U3','KEH U4','KEH M4','KEH U8','KEH U9']
    csclasses = {'CS 1043': (datetime.time(9,30),datetime.time(11)),
              'CS 2003': (datetime.time(10,30),datetime.time(12)),
              'CS 2123': (datetime.time(11,15),datetime.time(12,45)),
              'CS 3003': (datetime.time(8,15),datetime.time(11,30)),
              'CS 3353': (datetime.time(11),datetime.time(12)),
              'CS 4013': (datetime.time(13),datetime.time(14,45)),
              'CS 4063': (datetime.time(12,30),datetime.time(14,30)),
              'CS 4123': (datetime.time(14),datetime.time(15)),
              'CS 4163': (datetime.time(14),datetime.time(16,30)),
              'CS 4253': (datetime.time(12),datetime.time(16)),
    }
    print csclasses
    print scheduleRooms(ensrooms,csclasses)
    print scheduleRooms(ensrooms[:4],csclasses)