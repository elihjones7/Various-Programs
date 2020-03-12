# Eli Jones
# Starter code to HW3 Q1.

import urllib
from collections import deque


def getLinks(url, baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    # import the HTML parser package
    try:
        from BeautifulSoup import BeautifulSoup
    except:
        print 'You must first install the BeautifulSoup package for this code to work'
        raise
    # fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.urlopen(url).read())
    # pull out the links from the HTML and return
    return [baseurl + a["href"].encode('ascii', 'ignore') for a in soup.findAll('a')]


def print_dfs(url):
    """
    Print all links reachable from a starting **url**
    in depth-first order
    """
    #
    g = {}
    hist, stack = set(), []
    stack.append(url)
    i = 1
    while stack:
        temp = stack.pop()
        if temp in hist: continue
        hist.add(temp)
        list = getLinks(temp)
        while list:
            tmp = list.pop()
            stack.append(tmp)
        g[i] = temp
        i += 1
    print g
    #I used the code from the slides. Not sure if I need to cite it or not

def print_bfs(url):
    """
    Print all links reachable from a starting **url**
    in breadth-first order
    """
    #
    g = {}
    visited, stack = set(), deque()
    stack.append(url)
    i = 1
    while stack:
        temp = stack.popleft()
        if temp not in visited:
            visited.add(temp)
            list = getLinks(temp)
            stack.extend(list)
            g[i] = temp
            i += 1
    print g
    #the code from the slides helped. Not sure if I need to cite it or not

def find_shortest_path(url1, url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
    check = deque()
    path = []
    list = getLinks(url1)
    path.append(url1)
    while list:
        check.append(list.pop())
    tmp = check.pop()
    while tmp != url2:
        if tmp in path:
            print "Path not available"
            break
        else:
            templist = getLinks(tmp)
            if url2 in templist:
                path.append(tmp)
                path.append(url2)
                print path
                break
            check.extend(templist)
            path.append(tmp)
            tmp = check.popleft()

def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    #
    path = []
    check = deque()
    path.append(start_url)
    list = getLinks(start_url)
    while list:
        check.append(list.pop())
    while check:
        tmp = check.pop()
        if tmp in path:
            break
        else:
            path.append(tmp)
            loader = getLinks(tmp)
            while loader:
                check.append(loader.pop())
    print len(path)
    print path


if __name__ == "__main__":
    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print "*********** (a) Depth-first search   **********"
    print_dfs(starturl)
    print "*********** (b) Breadth-first search **********"
    print_bfs(starturl)
    print "*********** (c) Find shortest path between two URLs ********"
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    print "*********** (d) Find the longest shortest path from a starting URL *****"
    find_max_depth(starturl)