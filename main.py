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


def combinedTranscript(fetched_transcript):#This function combines all the text snippets in one string
    combined_text = ""#This string will hold all the combined text
    for snippet in fetched_transcript:#Loop through each snippet in the fetched transcript#".
        snip = snippet.text.split()#Splits the text of each snippet into individual words. Splits at spaces.".text" is an object attribute of the snippet dictionary
        #'text' holds the text of each snippet in the dictionary. We must specify that access to the text value otherwise it will split the entire dictionary including timing metadata
        for word in snip:#iterates through each word in the snippet
            combined_text += word + " "#Add the word followed by a space for each snippet to the empty string

    combined_text = combined_text.strip()#Removes spaces at the beginning and end of string
    return combined_text#return the combined text in one string

print(combinedTranscript(fetched_transcript))#prints the transcript in one string
    





