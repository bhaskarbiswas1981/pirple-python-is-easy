'''
This multi-line comments.
'''
#Songs Meta-data variables
song_name="Big Yellow Taxi (Joni Mitchell cover)"
artist="Joni Mitchell"
composer="Joni Mitchell"
year=1970
genre="Folk rock; pop; folk;"
BPM=126
grouping="Earthprogram Music(one-stop)"
comments="Contact info for licensing party"
album="LyricFiiind"
album_artist=""
disc_number=0
track=0

#Declare functions
def funcGenre(songGenere):
    genre=songGenere
    return genre

def funcArtist(songArtist):
    artist=songArtist
    return genre

def funcYear(songYear):
    year=songYear
    return genre



#Prnt all the songs meta-data
print(song_name)
print(artist)
print(composer)
print(year)
print(genre)
print(BPM)
print(grouping)
print(comments)
print(album)
print(album_artist)
print(disc_number)
print(track)

print(funcGenre("I Want My Now"))
print(funcArtist("Hollywood Vampires"))
print(funcYear(2018))
