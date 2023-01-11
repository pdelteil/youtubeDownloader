import urllib.request
import json
import math
import sys

#Get list of videos from Youtube channel
def getVideos(maxResults, uploadId, key,nextPageToken, videosOutput):
    videos = []
    # construct the API url
    urld = searchURL+"/playlistItems?part=snippet%2CcontentDetails&maxResults="+maxResults+"&playlistId="+uploadId+"&key="+key+"&pageToken="+nextPageToken   
    # open the API url and read the response
    with urllib.request.urlopen(urld) as url:
        datad = json.loads(url.read())
    # print the URL for debugging purposes
    print(urld)
 
    # loop through the items in the response
    for data in datad['items']:
        # get the title and video id
        ntitle =  data['snippet']['title']
        nlink = data['contentDetails']['videoId']
        # add the video information to the output list
        videosOutput.append([nlink,ntitle])
    # check if there's a next page token
    if 'nextPageToken' in datad:
       nextPageToken = datad['nextPageToken']
       #recursive call     
       getVideos(maxResults, uploadId, key, nextPageToken, videosOutput)

# API key for accessing the YouTube API
key = "API_KEY"
# base URL for a YouTube video
videoURL = "http://www.youtube.com/watch?v="
# base URL for the YouTube API
searchURL = "https://www.googleapis.com/youtube/v3"
# maximum number of results to retrieve per API call
maxResults= "50"
# variable to keep track of the next page token
nextPageToken = ""

#List of channels : mention if you are pasting channel id or username - "id" or "forUsername"
ytids = []
# open the input file containing the list of channels
with open(sys.argv[1]) as file:
    ytids = file.read().splitlines() 
file.close()     
videos = []

# loop through the list of channels
for ytid in ytids:
    # construct the API url to get the channel's details
    urld = searchURL+"/channels?part=contentDetails&id="+ytid+"&key="+key     
    # open the API url and read the response
    with urllib.request.urlopen(urld) as url:
        datad = json.loads(url.read())
    # print the response for debugging purposes
    print(datad)
    # get the channel's uploads details
    uploadsdet = datad['items']
  
# loop through the videos and print their URLs and titles
for link,title in videos:
    print(videoURL+link, title)
