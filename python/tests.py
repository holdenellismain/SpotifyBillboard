from testfuncs import *
from spotifyfuncs import *

'''
TESTS FOR SEARCH FUNCTION
'''

#random old songs
check_info("When", "Kalin Twins")
check_info("Just A Dream", "Jimmy Clanton And His Rockets")
check_info("The Rubberband Man", "The Spinners")

#random sample of pop songs
check_info("I Knew You Were Trouble", "Taylor Swift")
check_info("Nothing's Gonna Stop Us Now", "Starship")
check_info("Behind These Hazel Eyes", "Kelly Clarkson")

#songs with features
artist1 = "Post Malone Featuring Morgan Wallen"
artist1 = remove_feature(artist1)
check_info("I Had Some Help", artist1)
artist2 = "Future, Metro Boomin & Kendrick Lamar"
artist2 = remove_feature(artist2)
check_info("Like That", artist2)

#songs with / in the title
check_info("24/7", "Kevon Edmonds")
check_info("Candle In The Wind 1997/Something About The Way You Look Tonight", "Elton John")

#songs with ' in the title
check_info("You Don't Know My Name", "Alicia Keys")
check_info("I'll Be Missing You", "Puff Daddy")
check_info("Frontin'", "Pharrell")
check_info("What's Left Of Me", "Nick Lachey")

#kanye being weird, returns none
check_info("Carnival", "Â¥$: Ye & Ty Dolla $ign Featuring Rich The Kid & Playboi Carti")

'''
TESTS FOR AVERAGE_ATTRIBUTES
'''

#get an array of ids for a playlist
id1 = "52nF3mpxjvn5jvBh3XlDDb"
id2 = "37i9dQZF1DWVqfgj8NZEp1"
header = get_auth_header()
output = song_ids_playlist(id2, header)
playlist_ids = []
for song in output:
    playlist_ids.append(song["track"]["id"])
#remove null values
playlist_ids = remove_null(playlist_ids)
#testing average function
attributes = average_attributes(playlist_ids, header)
print_attributes(attributes)
