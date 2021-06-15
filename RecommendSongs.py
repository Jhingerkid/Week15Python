import requests


def makeSearchRequest():
    url = "https://shazam.p.rapidapi.com/search"
    querystring = {"term": inputSong,
                   "locale": "en-US", "offset": "0", "limit": "5"}
    headers = {
        'x-rapidapi-key': "9b689232b2mshb9760bb5da27bf9p14e4a3jsnda3498b3e945",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }
    searchResponse = (requests.request("GET",
                      url, headers=headers, params=querystring).json())
    return searchResponse


def makeRecommendationRequest():
    url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    querystring = {"key": selectedKey, "locale": "en-US"}
    headers = {
               'x-rapidapi-key':
               "9b689232b2mshb9760bb5da27bf9p14e4a3jsnda3498b3e945",
               'x-rapidapi-host': "shazam.p.rapidapi.com"
    }
    recommendationResponse = (requests.request("GET",
                              url, headers=headers, params=querystring).json())
    return recommendationResponse


def makeSongList(data):
    count = 0
    songList = []
    for x in data:
        songTitle = data['tracks']['hits'][count]['track']['title']
        songArtist = data['tracks']['hits'][count]['track']['subtitle']
        songEntry = str(count+1) + ". " + songTitle + " by " + songArtist
        songList.append(songEntry)
        count = count + 1
    return songList


def makeSongKeys(data):
    keyCount = 0
    songKeys = []
    for x in data:
        songKey = data['tracks']['hits'][keyCount]['track']['key']
        songKeys.append(songKey)
        keyCount = keyCount + 1
    return songKeys


def displaySongs():
    print("Which one did you mean?")
    for song in songResults:
        print(song)
    selectedSong = int(input())
    return selectedSong-1


def displayRecommendedSongs(recSongs):
    print("We recommend the following:")
    tracks = recSongs['tracks']
    for song in tracks:
        recSongTitle = song['title']
        recSongArtist = song['subtitle']
        print(f'{recSongTitle} by {recSongArtist}')
    return


inputSong = input("What song are you obsessively listening to right now?\n")
res = makeSearchRequest()
songResults = makeSongList(res)
songKeys = makeSongKeys(res)
selectedKey = songKeys[displaySongs()]
recommendedSongs = makeRecommendationRequest()
displayRecommendedSongs(recommendedSongs)
