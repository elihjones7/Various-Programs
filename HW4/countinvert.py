#Eli Jones
# Starter Code for Counting Inversions, Q1 HW4
# CS 2123, The University of Tulsa

from collections import deque #i treated the sequence like a list and didn't see the need to use these
import itertools


def mergeandcount(lft, rgt):
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """
    curr1 = 0 #lft pointer
    curr2 = 0 #rgt pointer
    count = 0 #counter for inversions
    seq = []  #sorted combined sequence
    while curr1<len(lft) and curr2<len(rgt):
        a = lft[curr1]
        b = rgt[curr2]
        if a < b: #element in a is smaller
            seq.append(a) #add a to the result
            curr1 += 1 #increment through lft by 1
        else: #element in b is smaller
            seq.append(b) #add b to result
            print b, " conflicts with ", a
            count = count + (len(lft) - curr1) #adding the length of whats left in the list to the counter
            curr2 += 1 #increment through rgt by 1
    if len(rgt) == curr2:#if the right side ran out of values first
        seq.extend(lft[curr1:]) #add the remainder of the list
    if len(lft) == curr1: #if the left side ran out of values first
        seq.extend(rgt[curr2:]) #add the remainder of the list
    return (count, seq)
def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    if len(seq) == 1: #if the length of the sequence is 1
        return (0, seq) #there are no inversions and it is sorted
    mid = len(seq)/2 #middle index
    left = seq[:mid]  #left half of the list
    right = seq[mid:] #right half of the list
    ltup = sortandcount(left) #sort left
    rtup = sortandcount(right) #sort right
    mtup =  mergeandcount(ltup[1], rtup[1]) #merge left and right sides
    count = ltup[0] + rtup[0] + mtup[0] #get the inversion counts from left right and merge
    return (count ,mtup[1])

if __name__ == "__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (5, "Cake: I Will Survive"),
              (6, "Aretha Franklin: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (8, "Coldplay: Clocks"),
              (9, "Nickelback: Gotta be Somebody"),
              (10, "Garth Brooks: Friends in Low Places")]
    songs2 = [(3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (8, "Coldplay: Clocks"),
              (6, "Aretha Franklin: I Will Survive"),
              (5, "Cake: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (9, "Nickelback: Gotta be Somebody"),
              (10, "Garth Brooks: Friends in Low Places")]
    songs3 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (6, "Aretha Franklin: I Will Survive"),
              (5, "Cake: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (8, "Coldplay: Clocks"),
              (10, "Garth Brooks: Friends in Low Places"),
              (9, "Nickelback: Gotta be Somebody")]
    print seq1
    print "# Inversions: %i\n" % sortandcount(seq1)[0]
    print seq2
    print "# Inversions: %i\n" % sortandcount(seq2)[0]
    print seq3
    print "# Inversions: %i\n" % sortandcount(seq3)[0]
    print songs1
    print "# Inversions: %i\n" % sortandcount(songs1)[0]
    print songs2
    print "# Inversions: %i\n" % sortandcount(songs2)[0]
    print songs3
    print "# Inversions: %i\n" % sortandcount(songs3)[0]
