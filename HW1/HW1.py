# Eli Jones and William Grantham
# Python implementation of stable matching problem
# Homework 1 Starter Code
# CS 2123 last modified 9/6/17

def gs(men, women, pref):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    # preprocessing
    ## build the rank dictionary
    rank = {}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m] = i
            i += 1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)  # initially all men and women are free
    numpartners = len(men)
    S = {}  # build dictionary to store engagements

    # run the algorithm
    while freemen:
        m = freemen.pop()
        # get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m] += 1
        if w not in S:
            S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S


def gs_block(men, women, pref, blocked):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of preferred names in sorted order)
            blocked (list of (man,woman) tuples that are unacceptable matches)
    Output: dictionary of stable matches
    """
    rank = {}
    for w in women:
        rank[w] = {}
        i = 1
        for m in pref[w]:
            rank[w][m] = i
            i += 1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)  # initially all men and women are free
    numpartners = len(men)
    S = {}  # build dictionary to store engagements

    # run the algorithm
    while freemen:
        m = freemen.pop()
        # get the highest ranked woman that has not yet been proposed to
        w = pref[m][prefptr[m]]
        prefptr[m] += 1
        test_block = (m,w)
        if w not in S:
            if test_block not in blocked:
                S[w] = m
        else:
            mprime = S[w]
            if rank[w][m] < rank[w][mprime]:
                S[w] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
    return S


def gs_tie(men, women, preftie):
    """
    Gale-shapley algorithm, modified to exclude unacceptable matches
    Inputs: men (list of men's names)
            women (list of women's names)
            pref (dictionary of preferences mapping names to list of sets of preferred names in sorted order)
    Output: dictionary of stable matches
    """
    rank = {}
    for w in women:
        rank[w] = {}
        i = 1
        for m in preftie[w]:
            if len(m) > 1:
                while len(m):
                    rank[w][m.pop()] = i
            else:
                rank[w][m.pop()] = i
            i += 1
    ## create a "pointer" to the next woman to propose
    prefptr = {}
    for m in men:
        prefptr[m] = 0

    freemen = set(men)  # initially all men and women are free
    numpartners = len(men)
    S = {}  # build dictionary to store engagements

    # run the algorithm
    while freemen:
        m = freemen.pop()
        # get the highest ranked woman that has not yet been proposed to

        w = preftie[m][prefptr[m]]
        prefptr[m] += 1
        wom = w.pop()
        if wom not in S:
            S[wom] = m
            w.add(wom)
        else:
            w.add(wom)
            mprime = S[wom]
            if rank[wom][m] < rank[wom][mprime]:
                S[wom] = m
                freemen.add(mprime)
            else:
                freemen.add(m)
                if len(w) >= 2:
                    w.pop()
                    prefptr[m] -=1

    return S


if __name__ == "__main__":
    # input data
    themen = ['xavier', 'yancey', 'zeus']
    thewomen = ['amy', 'bertha', 'clare']

    thepref = {'xavier': ['amy', 'bertha', 'clare'],
               'yancey': ['bertha', 'amy', 'clare'],
               'zeus': ['amy', 'bertha', 'clare'],
               'amy': ['yancey', 'xavier', 'zeus'],
               'bertha': ['xavier', 'yancey', 'zeus'],
               'clare': ['xavier', 'yancey', 'zeus']
               }
    thepreftie = {'xavier': [{'bertha'}, {'amy'}, {'clare'}],
                  'yancey': [{'amy', 'bertha'}, {'clare'}],
                  'zeus': [{'amy'}, {'bertha', 'clare'}],
                  'amy': [{'zeus', 'xavier', 'yancey'}],
                  'bertha': [{'zeus'}, {'xavier'}, {'yancey'}, ],
                  'clare': [{'xavier', 'yancey'}, {'zeus'}]
                  }

    blocked = {('xavier', 'clare'), ('zeus', 'clare'), ('zeus', 'amy')}

    # eng
    match = gs(themen, thewomen, thepref)
    print match

    match_block = gs_block(themen, thewomen, thepref, blocked)
    print match_block

    match_tie = gs_tie(themen, thewomen, thepreftie)
    print match_tie