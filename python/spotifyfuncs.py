from dotenv import load_dotenv
import os
import base64
from requests import post
from requests import get
import urllib.parse
import json

#access id and secret from user's machine
load_dotenv()
id = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")

def get_token():
    '''
    requests and returns access token using client keys
    '''
    #convert keys to base 64 enconding
    auth_string = id + ":" + secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    #define parameters for html post request
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    
    #request
    result = post(url, headers=headers, data=data)

    json_result = json.loads(result.content) #convert result content to dictionary
    token = json_result["access_token"] #get token from result dictionary
    
    return token

def get_auth_header():
    '''
    helper function to create header for http requests
    '''
    token = get_token()
    return {"Authorization" : "Bearer " + token}

def song_ids_playlist(playlist_id, header):
    '''
    using a playlist id as input and a current token
    returns list of tracks from playlist
    '''
    url = "https://api.spotify.com/v1/playlists/" + playlist_id + f"/tracks" #field limits can be added here, documentation on web
    result = get(url, headers=header) #http request
    output = json.loads(result.content) #convert to dictionary
    return output["items"]

def remove_feature(artist):
    """
    helper function for search, removes the featured artist from the artist name
    might be a more efficient way of checking all of these?
    """
    #if featured artists is separated by the word "Featuring" (most common)
    location = artist.find("Feat")
    if location > 0:
        return artist[:location - 1]
    #if featured artists are separated by a comma
    location = artist.find(",")
    if location > 0:
        return artist[:location]
    #if featured artists are separated by &
    #sometimes bands will have this char but it is more commonly used for features
    location = artist.find("&")
    if location > 0:
        return artist[:location - 1]
    #pretty rare to have a feature separated by this, but more common in latin music
    #going to give errors for Lil Nas X singles...
    location = artist.find(" X ")
    if location > 0:
        return artist[:location]
    #also pretty rare
    location = artist.find(" x ")
    if location > 0:
        return artist[:location]
    #if there is no feature
    return artist

def clean_song_title(title):
    '''
    clean song title strings for search functionality
    '''
    title = title.replace("'", "") #makes query think string has ended (doesn't differentiate between " and ')
    #taylor's version
    location = title.find("(")
    if location > 0:
        return title[:location - 1]
    #from the vault + backstreet boys
    location = title.find("[")
    if location > 0:
        return title[:location - 1]
    #some old songs have two titles separated like this
    location = title.find("/")
    if location > 0:
        return title[:location]
    #title is normal
    return title

def search_for_song(title, artist, header):
    """
    searches spotify for a song using title and artist
    *artist should be a single artist, not including features
    returns the id if it exists/can be found
    returns None otherwise
    """
    title = clean_song_title(title)
    q = 'track:"' + title + '" artist:"' + artist + '"'
    q = urllib.parse.quote(q) #convert to ascii characters
    url = "https://api.spotify.com/v1/search?q=" + q + "&type=track&limit=1"
    result = get(url, headers=header) #http request
    output = json.loads(result.content) #convert to dictionary
    
    #no results from search
    if output["tracks"]["total"] == 0:
        return None
    #song was found, return the id
    return output["tracks"]["items"][0]["id"]

def info_from_id(song_id, header):
    """
    given an id, returns the song title and artist's name
    mostly for testing search functionality
    """
    if song_id == None:
        return None, None
    url = "https://api.spotify.com/v1/tracks/" + song_id
    result = get(url, headers=header)
    output = json.loads(result.content)
    return output["artists"][0]["name"], output["name"]

def average_attributes_helper(output, attribute):
    size = len(output["audio_features"])
    total = 0
    for i in range(size):
        if output["audio_features"][i] == None: #sometimes analysis will not exist and the array will have a null
            print("Missing audio features")
            size -= 1
        else:
            total += output["audio_features"][i][attribute]
    if size > 0:
        return total / float(size)
    return -1 #no tracks had analysis

def average_attributes(arr, header):
    '''
    takes an array of song ids
    returns the average duration, tempo, acousticness, and energy of the tracks

    gets rated limited sometimes which doesn't make sense because it's just 1 request
    '''
    #join into a string for url
    id_string = ",".join(arr)
    url = "https://api.spotify.com/v1/audio-features?ids=" + id_string
    result = get(url, headers=header)
    output = json.loads(result.content)
    
    #calculate means
    duration = average_attributes_helper(output, "duration_ms")
    acousticness = average_attributes_helper(output, "acousticness")
    energy = average_attributes_helper(output, "energy")

    #return array
    return [duration, acousticness, energy]

