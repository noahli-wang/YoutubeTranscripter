#Import youtube api and regex which allows to format and find the code of the YouTube video
import re
from youtube_transcript_api import YouTubeTranscriptApi

#This is the Youtube link
url = "https://www.youtube.com/watch?v=Z6nkEZyS9nA"

#Input Handling
#Gets the Youtube Code of any link that we give it, the link is everything after ?v= 
def fetchCode(url):
    #Uses regex to find either a ?=v or a / found within Youtube links and grabs 11 whatever characters after that
    code = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    #Now that we have the code, this finds if it matches with the url that we want
    matched = re.search(code,url)
    if(matched):
        #return the Youtube code if it matches
        return matched.group(1)
    
    else:
        return ValueError("This is not a valid YouTube URL")


#Find a way to get the transcript via the YouTube API library
video_id = fetchCode(url)
#This works I tested it
#print(video_id)


#This from the library website
youtubeAPI = YouTubeTranscriptApi()
#This returns a FetchedTranscript object, refer to link to see what it would look like 
fetched_transcript = youtubeAPI.fetch(video_id)
#This shows all the text as little snippets, run to see what it looks like
for snippet in fetched_transcript:
    print(snippet)





