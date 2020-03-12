#Eli Jones and William Grantham
#Starter code for HW5 Q1

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def playlist_transform(s,t,compareType="Song"):
    """
    Computes the edit distance for two playlists s and t, and prints the minimal edits
      required to transform playlist s into playlist t.
    Inputs:
    s: 1st playlist (format: list of (track name, artist, genre) triples)
    t: 2nd playlist (format: list of (track name, artist, genre) triples)
    compareType: String indicating the type of comparison to make.
       "Song" (default): songs in a playlist are considered equivalent if the
         (song name, artist, genre) triples match.
       "Genre": songs in a playlist are considered equivalent if the same genre is used.
       "Artist": songs in a playlist are considered equivalent if the same artist is used.
    Output: The minimum edit distance and the minimal edits required to transform playlist
      s into playlist t.
    """
    if(compareType is "Song"): x = 0
    if(compareType is "Artist"): x = 1
    if(compareType is "Genre"): x = 2
    chart = [[0 for z in range(len(t)+1)] for y in range(len(s)+1)]
    chart2 = [[0 for z in range(len(t)+1)] for y in range(len(s)+1)]
    sub, key = {}, {}
    sub[0], key[0] = "", ""
    for a in range(len(s)+1):
        chart[a][0] = a
    for b in range(len(t)+1):
        chart[0][b] = b
    for i in range(len(s)):
        sub[i+1] = s[i][x]
    for i in range(len(t)):
        key[i+1] = t[i][x]


    for i in range(1,len(s)+1):
        for j in range(1, len(t)+1):
            if(sub[i] == key[j]):
                match = chart[i-1][j-1]
                chart[i][j] = match
                chart2[i][j] = 1
            else:
                match = chart[i-1][j-1] +1
                insert = chart[i][j-1] +1
                delete = chart[i-1][j] +1
                if(match <= insert & match <= delete):
                    chart[i][j] = match
                    chart2[i][j] = 2

                elif(insert <= match & insert <= delete):
                    chart[i][j] = insert
                    chart2[i][j] = 3
                elif(delete <= insert & delete <= match):
                    chart[i][j] = delete
                    chart2[i][j] = 4
                else:
                    chart[i][j] = min(match, insert, delete)
    trip = chart2[len(s)][(len(t))]
    indx = len(s)
    indy = len(t)
    list = []
    while trip !=0:
        if trip == 1:
            trip = chart2[indx-1][indy-1]
            indx -=1
            indy-=1
            list.append("Keep it. Its a match")
        if trip == 2:
            trip = chart2[indx-1][indy-1]
            indx-=1
            indy-=1
            list.append("Substitution required")
        if trip == 3:#insertion
            trip = chart2[indx-1][indy]
            indx-=1
            list.append("Insertion required")
        if trip == 4:#deletion
            trip = chart2[indx][indy-1]
            indy-=1
            list.append("Deletion required")

    print "The edit distance is " + str(chart[len(s)][len(t)])
    while list:
        print list.pop()

if __name__=="__main__":
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues1.csv
    b1 = read_playlist("blues1.csv")
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues2.csv
    b2 = read_playlist("blues2.csv")
    print "Playlist 1"
    for song in b1:
        print song
    print "Playlist 2"
    for song in b2:
        print song
    print "Comparing playlist similarity by song"
    playlist_transform(b1,b2)
    print "Comparing playlist similarity by genre"
    playlist_transform(b1,b2,"Genre")
    print "Comparing playlist similarity by artist"
    playlist_transform(b1,b2,"Artist")
    #include your own playlists below
    classicrock = [("Fortunate Son", "Creedence Clearwater Revival", "Rock"), ("Welcome to the Jungle", "Guns N' Roses", "Rock"), ("Dust in the Wind", "Kansas", "Rock"), ("Smoke On The Water", "Deep Purple", "Rock")]
    irish = [("Star Of County Down", "The High Kings", "Folk"), ("The Fields of Athenry", "The Dubliners", "Folk"), ("Red is the Rose", "The High Kings", "Folk"), ("The Foggy Dew", "Young Dubliners", "Folk")]
    print "Comparing playlist similarity by song"
    playlist_transform(classicrock, irish)
    print "Comparing playlist similarity by genre"
    playlist_transform(classicrock,irish,"Genre")
    print "Comparing playlist similarity by artist"
    playlist_transform(classicrock,irish,"Artist")
