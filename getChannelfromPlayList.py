import urllib.request
import json
import math
import sys

# specify the API key
key = "API_KEY"
# URL for the channel of the playlists
videoURL = "http://www.youtube.com/channel/"
# base URL for the YouTube Data API
searchURL = "https://www.googleapis.com/youtube/v3"

# read list of playlist IDs from a file passed as an argument
playlistsIDs = []
with open(sys.argv[1]) as file:
      playlistsIDs = file.read().splitlines() 
file.close()     

# iterate through the playlist IDs
for id in playlistsIDs:
    # construct the full API URL, including the API key and the ID of the playlist
    urld = searchURL+"/playlists?part=snippet&id="+id+"&key="+key   
  
    # send a GET request to the API using urllib
    with urllib.request.urlopen(urld) as url:
        datad = json.loads(url.read())
  
    # extract the total number of results and channel ID from the response
    totalResults= datad['pageInfo']['totalResults']
    if int(totalResults) > 0:
        channelId = datad['items'][0]['snippet']['channelId']
        # print the URL of the channel
        print(videoURL+str(channelId)+"/videos")
    else:
        # print "not Found" if no results
        print("not Found")
