#Import youtube api and regex which allows to format and find the code of the YouTube video
import re
import youtube_transcript_api

#This is the Youtube link
url = "https://www.youtube.com/watch?v=Z6nkEZyS9nA"


#Gets the Youtube Code of any link that we give it, the link is everything after ?v= 
def fetchCode(url):
    #Uses regex to find either a ?=v or a / found within Youtube links and grabs 11 whatever characters after that
    code = r'(?:=v|\/)([0-9A-Za-z_-]11).*'

    #Now that we have the code, this finds if it matches with the url that we want
    matched = re.search(url,code)
    if(matched):
        return matched.group(1)
    
    else:
        return ValueError("This is not a valid YouTube URL")


